import json
import secrets
import string
import bs4
import openai
import tiktoken
import base64
import requests
from urllib.parse import urlparse
import argparse
common_style_classes = [
    # Bootstrap Classes
    "container",
    "row",
    "col",
    "btn",
    "btn-primary",
    "btn-secondary",
    "btn-success",
    "btn-danger",
    "btn-warning",
    "btn-info",
    "btn-light",
    "btn-dark",
    "btn-link",
    "text-primary",
    "text-secondary",
    "text-success",
    "text-danger",
    "text-warning",
    "text-info",
    "text-light",
    "text-dark",
    "text-muted",
    "bg-primary",
    "bg-secondary",
    "bg-success",
    "bg-danger",
    "bg-warning",
    "bg-info",
    "bg-light",
    "bg-dark",
    "bg-white",
    "bg-transparent",
    "border",
    "border-primary",
    "border-secondary",
    "border-success",
    "border-danger",
    "border-warning",
    "border-info",
    "border-light",
    "border-dark",
    "rounded",
    "rounded-circle",
    "rounded-pill",
    "rounded-0",
    "shadow",
    "d-none",
    "d-inline",
    "d-inline-block",
    "d-block",
    "d-table",
    "d-table-row",
    "d-table-cell",
    "text-center",
    "text-right",
    "text-left",
    "align-middle",
    "align-top",
    "align-bottom",
    "flex",
    "flex-row",
    "flex-column",
    "justify-content-start",
    "justify-content-end",
    "justify-content-center",
    "justify-content-between",
    "justify-content-around",
    "align-items-start",
    "align-items-end",
    "align-items-center",
    "align-items-baseline",
    "align-items-stretch",
    "text-nowrap",
    "overflow-auto",
    "position-static",
    "position-relative",
    "position-absolute",
    "position-fixed",
    "position-sticky",
    "sticky-top",
    "fixed-top",
    "fixed-bottom",
    "sr-only",

    # Tailwind CSS Classes
    "container",
    "mx-auto",
    "my-auto",
    "px-4",
    "py-2",
    "text-sm",
    "text-lg",
    "text-xl",
    "text-2xl",
    "text-3xl",
    "text-4xl",
    "text-5xl",
    "text-6xl",
    "font-bold",
    "font-semibold",
    "font-normal",
    "text-gray-100",
    "text-gray-200",
    "text-gray-300",
    "text-gray-400",
    "text-gray-500",
    "text-gray-600",
    "text-gray-700",
    "text-gray-800",
    "text-gray-900",
    "bg-gray-100",
    "bg-gray-200",
    "bg-gray-300",
    "bg-gray-400",
    "bg-gray-500",
    "bg-gray-600",
    "bg-gray-700",
    "bg-gray-800",
    "bg-gray-900",
    "border-gray-100",
    "border-gray-200",
    "border-gray-300",
    "border-gray-400",
    "border-gray-500",
    "border-gray-600",
    "border-gray-700",
    "border-gray-800",
    "border-gray-900",
    "rounded",
    "rounded-full",
    "rounded-md",
    "rounded-lg",
    "rounded-xl",
    "shadow",
    "shadow-sm",
    "shadow-md",
    "shadow-lg",
    "shadow-xl",
    "shadow-2xl",
    "block",
    "inline-block",
    "inline",
    "flex",
    "flex-row",
    "flex-col",
    "justify-start",
    "justify-end",
    "justify-center",
    "justify-between",
    "justify-around",
    "items-start",
    "items-end",
    "items-center",
    "items-baseline",
    "items-stretch",
    "text-left",
    "text-center",
    "text-right",
    "text-transparent",
    "text-current",
    "bg-transparent",
    "bg-current",
    "bg-black",
    "bg-white",
    "bg-gray-100",
    "bg-gray-200",
    "bg-gray-300",
    "bg-gray-400",
    "bg-gray-500",
    "bg-gray-600",
    "bg-gray-700",
    "bg-gray-800",
    "bg-gray-900",
    "bg-red-100",
    "bg-red-200",
    "bg-red-300",
    "bg-red-400",
    "bg-red-500",
    "bg-red-600",
    "bg-red-700",
    "bg-red-800",
    "bg-red-900",
    "bg-green-100",
    "bg-green-200",
    "bg-green-300",
    "bg-green-400",
    "bg-green-500",
    "bg-green-600",
    "bg-green-700",
    "bg-green-800",
    "bg-green-900",
    "bg-blue-100",
    "bg-blue-200",
    "bg-blue-300",
    "bg-blue-400",
    "bg-blue-500",
    "bg-blue-600",
    "bg-blue-700",
    "bg-blue-800",
    "bg-blue-900",
    "bg-yellow-100",
    "bg-yellow-200",
    "bg-yellow-300",
    "bg-yellow-400",
    "bg-yellow-500",
    "bg-yellow-600",
    "bg-yellow-700",
    "bg-yellow-800",
    "bg-yellow-900",
    "bg-indigo-100",
    "bg-indigo-200",
    "bg-indigo-300",
    "bg-indigo-400",
    "bg-indigo-500",
    "bg-indigo-600",
    "bg-indigo-700",
    "bg-indigo-800",
    "bg-indigo-900",
    "bg-purple-100",
    "bg-purple-200",
    "bg-purple-300",
    "bg-purple-400",
    "bg-purple-500",
    "bg-purple-600",
    "bg-purple-700",
    "bg-purple-800",
    "bg-purple-900",
    "bg-pink-100",
    "bg-pink-200",
    "bg-pink-300",
    "bg-pink-400",
    "bg-pink-500",
    "bg-pink-600",
    "bg-pink-700",
    "bg-pink-800",
    "bg-pink-900",
    "border",
    "border-transparent",
    "border-current",
    "border-black",
    "border-white",
    "border-gray-100",
    "border-gray-200",
    "border-gray-300",
    "border-gray-400",
    "border-gray-500",
    "border-gray-600",
    "border-gray-700",
    "border-gray-800",
    "border-gray-900",
    "border-red-100",
    "border-red-200",
    "border-red-300",
    "border-red-400",
    "border-red-500",
    "border-red-600",
    "border-red-700",
    "border-red-800",
    "border-red-900",
    "border-green-100",
    "border-green-200",
    "border-green-300",
    "border-green-400",
    "border-green-500",
    "border-green-600",
    "border-green-700",
    "border-green-800",
    "border-green-900",
    "border-blue-100",
    "border-blue-200",
    "border-blue-300",
    "border-blue-400",
    "border-blue-500",
    "border-blue-600",
    "border-blue-700",
    "border-blue-800",
    "border-blue-900",
    "border-yellow-100",
    "border-yellow-200",
    "border-yellow-300",
    "border-yellow-400",
    "border-yellow-500",
    "border-yellow-600",
    "border-yellow-700",
    "border-yellow-800",
    "border-yellow-900",
    "border-indigo-100",
    "border-indigo-200",
    "border-indigo-300",
    "border-indigo-400",
    "border-indigo-500",
    "border-indigo-600",
    "border-indigo-700",
    "border-indigo-800",
    "border-indigo-900",
    "border-purple-100",
    "border-purple-200",
    "border-purple-300",
    "border-purple-400",
    "border-purple-500",
    "border-purple-600",
    "border-purple-700",
    "border-purple-800",
    "border-purple-900",
    "border-pink-100",
    "border-pink-200",
    "border-pink-300",
    "border-pink-400",
    "border-pink-500",
    "border-pink-600",
    "border-pink-700",
    "border-pink-800",
    "border-pink-900",
    "rounded",
    "rounded-sm",
    "rounded-md",
    "rounded-lg",
    "rounded-xl",
    "rounded-2xl",
    "border-solid",
    "border-dashed",
    "border-dotted",
    "border-0",
    "border-2",
    "border-4",
    "border-8",
    "border-t",
    "border-r",
    "border-b",
    "border-l",
    "overflow-hidden",
    "overflow-auto",
    "overflow-x-hidden",
    "overflow-x-auto",
    "overflow-y-hidden",
    "overflow-y-auto",
    "relative",
    "absolute",
    "fixed",
    "inset-0",
    "inset-y-0",
    "inset-x-0",
    "top-0",
    "right-0",
    "bottom-0",
    "left-0",
    "z-0",
    "z-10",
    "z-20",
    "z-30",
    "z-40",
    "z-50",
    "bg-cover",
    "bg-contain",
    "bg-no-repeat",
    "bg-repeat",
    "bg-repeat-x",
    "bg-repeat-y",
]
unique_common_style_classes = list(set(common_style_classes))


# Hashing

class_map = {}


def generate_hash(length=4):
    # alphabetic characters
    alphanumeric_chars = string.ascii_letters
    hash = ''.join(secrets.choice(alphanumeric_chars) for _ in range(length))
    # Ensure that the hash is not already in use
    # if retrieve_class_name(hash) is None:
    #     hash = generate_hash(length)
    return hash


def get_short_hash(class_name, length=4):
    if class_name in class_map:
        return class_map[class_name]
    # Generate short unique hash value
    short_hash = generate_hash(length)
    # Map class name to short hash value
    class_map[class_name] = short_hash
    return short_hash


def retrieve_class_name(short_hash):
    for class_name, hash_value in class_map.items():
        if hash_value == short_hash:
            return class_name
    # Short hash value not found
    return None


# HTML TO JSON

new_format = dict()


def _debug(debug, message, prefix=''):
    """Print the given message if debugging is true."""
    if debug:
        print('{}{}'.format(prefix, message))
        # add a newline after every message
        print('')


def _record_element_value(element, json_output):
    """Record the html element's value in the json_output."""
    element = element.strip()
    if element != '\n' and element != '':
        if json_output.get('_value'):
            json_output['_values'] = [json_output['_value']]
            json_output['_values'].append(element)
            del json_output['_value']
        elif json_output.get('_values'):
            json_output['_values'].append(element)
        else:
            json_output['_value'] = element


def _iterate(
    html_section,
    json_output,
    count,
    debug,
    capture_element_values,
    capture_element_attributes,
    classInc,
    base_url,
    # xpath='/html'
):
    _debug(debug, '========== Start New Iteration ==========', '    ' * count)
    _debug(debug, 'HTML_SECTION:\n{}'.format(html_section))
    _debug(debug, 'JSON_OUTPUT:\n{}'.format(json_output))
    for part in html_section:
        if not isinstance(part, str):

            try:
                string_is_unicode = isinstance(part, unicode)

            except NameError as e:
                string_is_unicode = False

            finally:

                if not string_is_unicode:
                    EXLCUDE_TAGS = ['script', 'header',
                                    'iframe', 'style', 'svg']
                    if part.name not in EXLCUDE_TAGS:
                        # if index != 0:
                        #     xpath_current = xpath + '/' + part.name + '[' + str(index + 1) + ']'
                        # else:
                        #     xpath_current = xpath + '/' + part.name
                        if not json_output.get(part.name):
                            json_output[part.name] = list()

                        new_json_output_for_subparts = dict()
                        if part.attrs and capture_element_attributes:
                            if classInc:
                                attrs_to_include = {
                                    'id', 'href', 'class', 'src'}
                            else:
                                attrs_to_include = {'id', 'href', 'src'}
                            temp = {}
                            for attr in attrs_to_include:
                                if attr in part.attrs:
                                    if attr == 'class':
                                        classes = list()
                                        for cls in part.attrs['class']:
                                            if cls not in unique_common_style_classes:
                                                hash_className = get_short_hash(
                                                    cls)
                                                classes.append(hash_className)
                                        if classes:
                                            temp['class'] = classes
                                    elif attr == 'href':
                                        temp['href'] = part.attrs['href']
                                    elif attr == 'src':
                                        temp['src'] = ""
                                    elif attr == 'id':
                                        # check if part.attrs['id'] is not a array
                                        if isinstance(part.attrs['id'], list):
                                            temp['id'] = []
                                            for id in part.attrs['id']:
                                                hash_url = get_short_hash(id)
                                                temp['id'].append(hash_url)
                                        else:
                                            hash_url = get_short_hash(
                                                part.attrs['id'])
                                            temp['id'] = hash_url
                                    else:
                                        temp[attr] = part.attrs[attr]

                            # temp['xpath'] = part.xpath
                            if temp:
                                for key, value in temp.items():
                                    new_json_output_for_subparts[key] = value
                                # new_json_output_for_subparts['attr'] = temp
                        # if part.name == 'a':
                        #     # check if new_format['links'] is not empty and exists
                        #     if not new_format.get('links'):
                        #         new_format['links'] = []

                        #     new_format['links'].append({
                        #         **new_json_output_for_subparts,
                        #     })
                        count += 1
                        # check if new_json_output_for_subparts is not empty
                        # if new_json_output_for_subparts != {} or count < 3:
                        recursive_json_output = _iterate(
                            part,
                            new_json_output_for_subparts,
                            count,
                            debug=debug,
                            capture_element_values=capture_element_values,
                            capture_element_attributes=capture_element_attributes,
                            classInc=classInc,
                            base_url=base_url
                            # xpath=xpath_current
                        )
                        if recursive_json_output != None:
                            json_output[part.name].append(
                                recursive_json_output)

                else:
                    if capture_element_values:
                        _record_element_value(part, json_output)

        else:
            if capture_element_values:
                _record_element_value(part, json_output)
        if part.name == 'a':
            # check if new_format['links'] is not empty and exists
            if not new_format.get('links'):
                new_format['links'] = []
            if new_json_output_for_subparts.get('href') and new_json_output_for_subparts['href'].startswith('http') and not new_json_output_for_subparts['href'].startswith(base_url):
                continue
            else:
                new_format['links'].append({
                    **new_json_output_for_subparts,
                })

    if json_output:
        return json_output
    else:
        return None


def convert(
    html_string,
    debug=False,
    capture_element_values=True,
    capture_element_attributes=True,
    classInc=True,
    base_url=''
):
    """Convert the html string to json."""
    soup = bs4.BeautifulSoup(html_string, 'html.parser').body
    l = [child for child in soup.contents]
    return _iterate(
        l,
        {},
        0,
        debug=debug,
        capture_element_values=capture_element_values,
        capture_element_attributes=capture_element_attributes,
        classInc=classInc,
        base_url=base_url
    )


# HTML TO JSON Function


def from_html_to_json(html_string, deb=False, cev=True, cea=True, classInc=True, base_url=''):
    output_json = convert(html_string, debug=deb, capture_element_values=cev,
                          capture_element_attributes=cea, classInc=classInc, base_url=base_url)
    # save json to file
    with open('new_try.json', 'w') as f:
        json.dump(output_json, f)
    return [output_json, new_format]


# OPENAI

openai.api_key = "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"


def prompt_generator(data, url, save_to_file=True):
    # prompt making
    prompt_txt = open('final.prompt.txt', 'r').read()
    # replace {{ links }} with links_str and {{ currnet_url }} with url
    prompt_txt = prompt_txt.replace(
        '{{ data }}', json.dumps(new_format, separators=(',', ':')))
    prompt_txt = prompt_txt.replace('{{ current_url }}', url)

    # save prompt_txt to file
    if save_to_file:
        with open('temp.prompt.txt', 'w') as f:
            f.write(prompt_txt)

    return prompt_txt


def openai_chat(data):
    # get_token_size(prompt_txt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[{"role": "system", "content": 'You are ChatGPT, a large language model trained by OpenAI'},
                  {"role": "user", "content": data}
                  ])
    return response


def openai_content(data):
    return data['choices'][0]['message']['content']


# Token size and price

def get_token_size(txt, header=1200):
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    # enc = tiktoken.encoding_for_model("text-davinci-003")
    # enc = tiktoken.get_encoding("cl100k_base")
    encoded = enc.encode(txt)
    enc_size = len(encoded) + header
    return {'taken': enc_size, 'sm': {'left': 4000 - enc_size, 'price': enc_size / 1000 * 0.0015}, 'large':  {'left': 16000 - enc_size, 'price': enc_size / 1000 * 0.003}}


# Get SCRAPE DATA

username = 'freakstar03@gmail.com'
password = '540timms'

tokenNimble = base64.b64encode(
    f"{username}:{password}".encode("ascii")).decode("ascii")


def get_scrape_data(_url, unlimited=False):
    url = 'https://api.webit.live/api/v1/realtime/web'
    headers = {
        'Authorization': f'Basic {tokenNimble}=',
        'Content-Type': 'application/json'
    }
    data = {
        # Add your parameters here
        "url": _url,
        "render": True,
        "parse": True,
        "format": "html",
        "country": "ALL",
        "locale": "en"
    }
    response = requests.post(url, headers=headers, json=data)
    while unlimited:
        if response.status_code == 200:
            break
        response = requests.post(url, headers=headers, json=data)
    if not unlimited and response.status_code != 200:
        print('Error in getting data from Nimble')
        exit()
    return response


# Get Domain from URL with https

def extract_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return f"https://{domain}"


# CLI
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-U", "--Url", help="Scrape URL")

# Read arguments from command line
args = parser.parse_args()

if not args.Url:
    print("Please provide URL with -U or --Url")
    exit()

# Test
url_to_scrape = args.Url

# get scrape data
scrape_data = get_scrape_data(url_to_scrape).text
print('-> Fetched Data from Nimble')

# repeat until token size is less than 14000
# get html to json
iteration = 0
while True:
    if iteration == 0:
        print('-> converting html to json')
        html_to_json = from_html_to_json(scrape_data, deb=False, cev=True,
                                         cea=True, classInc=True, base_url=extract_domain(url_to_scrape))[1]
    if iteration == 1:
        print('Trying wo class')
        html_to_json = from_html_to_json(scrape_data, deb=False, cev=True,
                                         cea=True, classInc=False, base_url=extract_domain(url_to_scrape))[1]
    if iteration == 2:
        print('Trying wo value and class')
        html_to_json = from_html_to_json(scrape_data, deb=False, cev=False,
                                         cea=True, classInc=False, base_url=extract_domain(url_to_scrape))[1]

    if iteration == 3:
        print('Failed to reduce Token size')
        exit()
    # generate prompt
    gen_prompt = prompt_generator(html_to_json, url_to_scrape)

    # prompt token size
    token_size = get_token_size(gen_prompt)
    iteration += 1
    if (token_size['taken'] > 14000):
        print('Token size is greater than 14000')
        new_format = {}
    else:
        break
# get openai response
print('-> Calling OpenAI')
openai_response = openai_chat(gen_prompt)

print(openai_content(openai_response))
