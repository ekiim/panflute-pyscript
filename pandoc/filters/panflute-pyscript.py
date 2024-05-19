#!/usr/bin/env python
from panflute import CodeBlock, RawBlock, run_filter, debug, Div


def action(elem, doc):
    if isinstance(elem, CodeBlock):
        # debug(dir(elem.attributes))
        if "pyscript" in elem.classes:
            html_attr = 'type="py"'
        elif "pyeditor" in elem.classes:
            html_attr = 'type="py-editor"'
        elif "pyterminal" in elem.classes:
            html_attr = 'type="py" terminal worker'
        else:
            return
        for key, value in elem.attributes.items():
            html_attr += f' {key}="{value}"'
        script_element = RawBlock(
            text=(
                f"<script {html_attr}>\n" +
                elem.text +
                "\n</script>\n"
            ),
            format="html"
        )

        if "show" in elem.attributes:
            elem.classes = ["python", *elem.classes]
            return Div(
                elem,
                script_element,
            )
        return script_element


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
