# from requests_html import HTMLSession, HTML
#
#
# session = HTMLSession()
# r = session.get("https://www.tasteofhome.com/article/types-of-coffee/")
# contents = r.html.find(".entry-content")
#
# for content in contents:
#     coffee = content.find("h4", first=True).text
#     details = content.find("p", first=True).text
#     print(coffee)
#     print(details)


def article_writer(filename, mode: str = 'w'):
    num = int(input("How many article you want to write?\n"))
    heading = []
    details = []
    img_links = []
    links = []
    for i in range(num):
        print(f"Article {i + 1}")
        h = input("Heading: ")
        img = input("Link of the image: ")
        d = input("Details: ")
        link = input("Link for related sources: ")
        heading.append(h)
        img_links.append(img)
        details.append(d)
        links.append(link)
    articles = []
    articles.append(f"<div>")
    for co, detail, img, link in zip(heading, details, img_links, links):
        article = f"\t<h2 class=\"{co}\">\n\t{co}\n\t</h2>\n" \
               f"\t<img src=\"{img}\" alt=\"{co} width=\"50%\"\">\n" \
               f"\t<p>\n\t{detail}\n\t</p>\n" \
               f"\t<h3>\n\t<a href=\"{link}\" target=\"_blank\">Sources</a>\n\t</h3>\n" \
               f"\t<br/>\n"
        articles.append(article)
    articles.append(f"</div>")
    html = "\n".join(articles)
    with open(f"{filename}.html", mode) as f:
        f.write(html)


def table_maker(filename, mode: str = 'w'):
    """
    Create a n*m table in HTML
    :param filename: file name without extension
    :return: None
    """
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    table = []

    for i in range(rows):
        row = []
        for j in range(cols):
            val = input(f"Enter the element at row={i}, column={j}: ")
            f_val = f"\t\t<td>{val}</td>"
            row.append(f_val)
        r = "\n".join(row)
        r = f"\t<tr>\n{r}\n\t</tr>"
        table.append(r)
    table = "\n".join(table)
    table = f"<table style=\"border:2px solid black; border-spacing:25px\">\n{table}\n</table>"

    with open(f"{filename}.html", mode) as f:
        f.write(table)


def pandas2html(pandas_filepath, filename: "HTML file name that will be created",
                pandas_file_type: str = "csv", mode='w'):
    """
    Expected pandas file type are csv, excel
    :param pandas_filepath:
    :param filename:
    :param pandas_file_type:
    :return:
    """
    import pandas as pd
    import numpy as np
    panda = None
    if pandas_file_type == "csv":
        panda = pd.read_csv(pandas_filepath)
    elif pandas_file_type == "excel":
        panda = pd.read_excel(pandas_filepath)

    panda.replace(np.nan, "", inplace=True)
    head = [i for i in panda.columns]
    head.insert(0, "")
    index = [j for j in panda.index]
    rows = [f"<table style=\"border:2px solid black; border-spacing:25px\">"]
    # Head of the table
    for _ in range(1):
        row = [f"\t<tr>"]
        for k in head:
            temp = f"\t\t<th>\n\t\t\t{k}\n\t\t</th>"
            row.append(temp)
        row.append(f"\t</tr>")
        r = "\n".join(row)
        rows.append(r)

    head.pop(0)
    for m in index:
        row = [f"\t<tr>"]
        temp = f"\t\t<th>\n\t\t\t{m}\n\t\t</th>"
        row.append(temp)
        for n in head:
            temp = f"\t\t<td>\n\t\t\t{panda.loc[m, n]}\n\t\t</td>"
            row.append(temp)
        row.append(f"\t</tr>")
        r = "\n".join(row)
        rows.append(r)
    rows.append("</table>")
    table = "\n".join(rows)
    with open(f"{filename}.html", mode) as f:
        f.write(table)


def numpy2html(array, filename="None", mode: str = 'w', cls: str = "table"):
    table = [f"<table class=\"{cls}\">"]
    for i in range(len(array[:, 0])):
        row = ["\t<tr>"]
        for j in range(len(array[0, :])):
            temp = F"\t\t<td class=\"array{str(array[i, j])}\">\n\t\t\t{array[i, j]}\n\t\t</td>"
            row.append(temp)
        row.append("\t</tr>")
        merge = "\n".join(row)
        table.append(merge)
    table.append("</table>")
    data = "\n".join(table)
    # with open(f"{filename}.html", mode) as f:
    #     f.write(data)
    return data


def create_html_page(body_data: list, title: str, css_file_name="style.css"):
    start = f"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<title>{title}</title>" \
            f"\n\t<link rel=\"stylesheet\" href={css_file_name}>\n</head>\n<body>"
    header = f"<header><h1>{title}</h1></header>"
    end = "</body>\n</html>"
    data = "\n".join(body_data)
    final_html_code = "\n".join([start, header, data, end])
    return final_html_code


if __name__ == "__main__":
    # table_maker("htmltable")
    # article_writer("htmlarticle")
    pandas2html("updated data.csv", "ud", "csv")
