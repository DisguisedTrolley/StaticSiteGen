import os
import shutil

from md_to_html import extract_title, markdown_to_html


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path}...")

    md = open(from_path)
    templ = open(template_path)

    md_file = md.read()
    templ_file = templ.read()

    md.close()
    templ.close()

    md_to_html_file = markdown_to_html(md_file)
    title = extract_title(md_file)

    final_html = templ_file.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", md_to_html_file)

    # Check if the directory exits.
    dir = os.path.dirname(dest_path)
    if not os.path.exists(dir):
        os.makedirs(dir)

    # fn_ext = os.path.basename(from_path)
    # fn = fn_ext.split(".")[0]

    html_file = open(dest_path, "w")
    html_file.write(final_html)
    html_file.close()

    return


"""
Retrieve markdown file at the given location, convert it to html, insert it into the template.
Return the final html template.
"""


def complete_html_file(path: str, template_dir: str) -> str:
    # Open md file with.
    f = open(path)
    md_file = f.read()
    f.close()

    html = markdown_to_html(md_file)
    title = extract_title(md_file)

    f_templ = open(template_dir)
    templ = f_templ.read()
    f_templ.close()

    final_html = templ.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html)

    return final_html


def generate_page_recursive(content_dir: str, dest_dir: str, template_dir: str) -> None:
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    contents = os.listdir(content_dir)

    if not contents:
        return

    for content in contents:
        content_path = os.path.join(content_dir, content)

        if os.path.isfile(content_path):
            # For now let's just recursively copy the contents,
            # Converting md to html will be done later.

            html_file = complete_html_file(path=content_path, template_dir=template_dir)

            new_file_instance = open(f"{dest_dir}/index.html", "w")
            new_file_instance.write(html_file)
            new_file_instance.close()

            continue

        dest_dir_url = f"{dest_dir}/{content}"
        if os.path.exists(dest_dir_url):
            shutil.rmtree(dest_dir_url)

        os.makedirs(dest_dir_url)
        generate_page_recursive(f"{content_dir}/{content}", dest_dir_url, template_dir)
