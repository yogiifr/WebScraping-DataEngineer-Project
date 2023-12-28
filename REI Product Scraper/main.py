#
import httpx
from selectolax.parser import HTMLParser
import time
from urllib.parse import urljoin
from dataclasses import asdict, dataclass, fields
import json
import csv

#
@dataclass
class Item:
    name: str
    item_num: str
    price: str
    rating: float

#
def get_html(url, **kwargs):
    headers     = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    if kwargs.get("page"):
        response    = httpx.get(url + str(kwargs.get("page")), headers=headers, follow_redirects=True)
    else:
        response    = httpx.get(url, headers=headers, follow_redirects=True)

    print(response.status_code)

    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}. Page Limit Exceeded")
        return False

    html        = HTMLParser(response.text)
    return html

#
def parse_search_page(html):
    products = html.css("li.VcGDfKKy_dvNbxUqm29K")
    
    for product in products:
        yield urljoin("https://www.rei.com/", product.css_first("a").attributes["href"])

#
def clean_data(value):
    chars_to_remove = ['$', "Item", '#']
    for char in chars_to_remove:
        if char in value:
            value = value.replace(char, '')
    return value.strip()

#
def extract_text(html, sel):
    try:
        text = html.css_first(sel).text()
        return clean_data(text)
    except AttributeError:
        return None
    
#
# class - . | id - #
def parse_item_page(html):
    new_item = Item(
        name    = extract_text(html, 'h1#product-page-title'),
        item_num= extract_text(html, 'span#product-item-number'),
        price   = extract_text(html, 'span#buy-box-product-price'),
        rating  = extract_text(html, 'span.cdr-rating__number_13-5-3'),
    )
    return asdict(new_item)

#
def export_to_json(products):
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    print('Saved to JSON')

#
def export_to_csv(products):
    field_names = [field.name for field in fields(Item)]
    with open('products.csv', 'w') as f:
        writer = csv.DictWriter(f, field_names)
        writer.writeheader()
        writer.writerows(products)
    print('Saved to CSV')

#
def append_to_csv(product):
    field_names = [field.name for field in fields(Item)]
    with open('appendcsv.csv', 'a') as f:
        writer = csv.DictWriter(f, field_names)
        writer.writerow(product)

#
def main():
    products = []

    #All Saving Deals Product
    baseurl = "https://www.rei.com/f/scd-outlet?page=" 
    
    for x in range(1,2):
        print(f"Gathering Product - Page: {x}")
        html = get_html(baseurl, page=x)
        if html is False:
            break
        product_urls = parse_search_page(html)
        for url in product_urls:
            print(url)
            html = get_html(url)
            products.append(parse_item_page(html))
            time.sleep(0.5)
    
    # for product in products:
    #     print(product)

    export_to_json(products)
    export_to_csv(products)

if __name__ == "__main__":
    main()

