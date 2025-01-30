import os
import shutil

from gen_page import generate_page_recursive


def copy_static_to_public(src_dir: str, dst_dir: str) -> None:
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    # List all the files in the directory
    entities = os.listdir(src_dir)

    for entity in entities:
        static_path = os.path.join(src_dir, entity)
        dst_path = os.path.join(dst_dir, entity)

        if os.path.isfile(static_path):
            shutil.copy(static_path, dst_path)

        else:
            copy_static_to_public(static_path, dst_path)


def main():
    root_dir = os.getcwd()
    src = os.path.join(root_dir, "static")
    dst = os.path.join(root_dir, "public")
    template = os.path.join(root_dir, "template.html")

    if os.path.exists(dst):
        shutil.rmtree(dst)
    copy_static_to_public(src, dst)

    # generate_page(
    #    from_path=f"{root_dir}/content/index.md",
    #    template_path=f"{root_dir}/template.html",
    #    dest_path=f"{root_dir}/public/index.html",
    # )

    generate_page_recursive(
        content_dir=f"{root_dir}/content", template_dir=template, dest_dir=dst
    )


if __name__ == "__main__":
    main()
