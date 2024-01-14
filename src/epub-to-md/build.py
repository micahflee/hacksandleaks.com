#!/usr/bin/env python3


def simplify_markdown(input_text):
    # Split the text into lines
    lines = input_text.split("\n")

    # Process each line
    for i, line in enumerate(lines):
        print(f"Processing line {i}: {line}")

        # Remove extra stuff after code block
        if line.startswith("```"):
            lines[i] = line[:3]

        # Process URL links
        start_index = line.find("[*https://")
        end_index = line.find("*](https://", start_index)
        if start_index != -1 and end_index != -1:
            url = line[end_index + 3 : line.find(")", end_index)]
            line = line[:start_index] + url + line[line.find(")", end_index) + 1 :]
            lines[i] = line

        # Remove Xref links but keep the text, including removing the braces part from Xrefs
        start_index = line.find("[[")
        while start_index != -1:
            # Find the closing part of the Xref link
            end_index = line.find(")]", start_index)
            if end_index == -1:
                end_index = line.find("),]", start_index)
            brace_index = line.find("}", end_index) if end_index != -1 else -1

            # Remove the Xref link
            if end_index != -1 and brace_index != -1:
                text_to_keep = line[start_index + 2 : line.find("](", start_index)]
                line = line[:start_index] + text_to_keep + line[brace_index + 1 :]
                lines[i] = line
            else:
                break
            start_index = line.find("[[")

        # Check if the line is a section header
        if line.startswith("#"):
            # Remove backticks, braces, and empty links, then trim whitespace
            line = line.replace("`", "")  # Remove backticks
            while "{" in line and "}" in line:
                start_brace = line.find("{")
                end_brace = line.find("}", start_brace)
                if end_brace != -1:
                    line = line[:start_brace] + line[end_brace + 1 :]
                else:
                    break
            line = line.replace("[]", "")  # Remove empty links
            line = line.strip()  # Trim whitespace
            lines[i] = line

        # Remove ':::' lines
        elif line.startswith(":::"):
            lines[i] = ""
        
        ## Convert "[ENTER]{.small}" to "**ENTER**"
        if "[ENTER]{.small}" in line:
            line = line.replace("[ENTER]{.small}", "**ENTER**")
            lines[i] = line

        ## Replace notes
        if line.startswith("> [`NOTE`{.sample .SANS_Dogma_OT_Bold_B_21}]{.NoteHead}"):
            lines[i] = "**NOTE**"
        if line.startswith("[`WARNING`{.sample .SANS_Dogma_OT_Bold_B_21}]{.NoteHead}"):
            lines[i] = "**WARNING**"

        ## Remove some extra font stuff
        for s in [
            "{.sample .SANS_TheSansMonoCd_W5Regular_11}",
            "{.sample .SANS_TheSansMonoCd_W7Bold_B_11}",
            "{.sample .SANS_Futura_Std_Book_Oblique_I_11}",
            "{.sample .SANS_TheSansMonoCd_W5Regular_Italic_I_11}",
            "{.sample .SANS_TheSansMonoCd_W7Bold_Italic_BI_11}",
            "{.sample .SANS_Futura_Std_Book_11}",
            "`<wbr>`{=html}`</wbr>`{=html}"
        ]:
            if s in line:
                line = line.replace(s, "")
                lines[i] = line

        ## Replace keys
        if "[TAB]{.small}" in line:
            line = line.replace("[TAB]{.small}", "**TAB**")
            lines[i] = line
        if "[ENTER]{.small}" in line:
            line = line.replace("[ENTER]{.small}", "**ENTER**")
            lines[i] = line
        if "[RETURN]{.small}" in line:
            line = line.replace("[RETURN]{.small}", "**RETURN**")
            lines[i] = line
        if "[HOME]{.small}" in line:
            line = line.replace("[HOME]{.small}", "**HOME**")
            lines[i] = line
        if "[END]{.small}" in line:
            line = line.replace("[END]{.small}", "**END**")
            lines[i] = line
        if "[CONTROL]{.small}" in line:
            line = line.replace("[CONTROL]{.small}", "**CONTROL**")
            lines[i] = line
        if "[CTRL]{.small}" in line:
            line = line.replace("[CTRL]{.small}", "**CTRL**")
            lines[i] = line
        if "[z]{.greek_wingdings}" in line:
            line = line.replace("[z]{.greek_wingdings}", "⌘")
            lines[i] = line

    # Rejoin lines
    output_text = "\n".join(lines)

    # Strip more stuff
    for s in [
        "{.sample\n.SANS_TheSansMonoCd_W5Regular_11}",
        "{.sample\n.SANS_TheSansMonoCd_W7Bold_B_11}",
        "{.sample\n.SANS_Futura_Std_Book_Oblique_I_11}",
        "{.sample\n.SANS_TheSansMonoCd_W5Regular_Italic_I_11}",
        "{.sample\n.SANS_TheSansMonoCd_W7Bold_Italic_BI_11}",
        "{.sample\n.SANS_Futura_Std_Book_11}"
    ]:
        output_text = output_text.replace(s, "")

    # Strip stuff like this: []{#chapter5.xhtml#pg_131 role="doc-pagebreak" type="pagebreak" aria-label=" Page 131. "}
    start_index = output_text.find("[]{#chapter")
    while start_index != -1:
        end_index = output_text.find("}", start_index)
        output_text = output_text[:start_index] + output_text[end_index + 1 :]
        start_index = output_text.find("[]{#chapter")
    
    # Strip css classes
    start_index = output_text.find("{.")
    while start_index != -1:
        end_index = output_text.find("}", start_index)
        output_text = output_text[:start_index] + output_text[end_index + 1 :]
        start_index = output_text.find("{.")

    # Strip figure ids
    start_index = output_text.find("{#fig")
    while start_index != -1:
        end_index = output_text.find("}", start_index)
        output_text = output_text[:start_index] + output_text[end_index + 1 :]
        start_index = output_text.find("{#fig")
    
    # Fix figure links, to change "[Figure 10-2](#chapter10.xhtml#fig10-2)" to "Figure 10-2"
    start_index = output_text.find("[Figure")
    while start_index != -1:
        end_index = output_text.find("]", start_index)
        figure_name = output_text[start_index + 1 : end_index]
        end_index = output_text.find(")", start_index)
        output_text = output_text[:start_index] + figure_name + output_text[end_index + 1 :]
        start_index = output_text.find("[Figure")

    # Remove newslines after NOTE and WARNING
    output_text = output_text.replace("**NOTE**\n\n*", "**NOTE** *")
    output_text = output_text.replace("**WARNING**\n\n*", "**WARNING** *")

    # Arrows
    output_text = output_text.replace("[▸]{.MenuArrow}", " ▸ ")

    # Add captions to figures "![`Figure 10-1: The freshly installed BlueLeaks Explorer app`](media/images/Figure10-1.png)"
    start_index = output_text.find("![`Figure")
    while start_index != -1:
        end_index = output_text.find("`", start_index + 3)
        caption = output_text[start_index + 3 : end_index]
        media_start_index = output_text.find("(", start_index)
        media_end_index = output_text.find(")", start_index)
        media = output_text[media_start_index + 1 : media_end_index]
        output_text = output_text[:start_index] + f"![{caption}]({media})  \n*{caption}*" + output_text[media_end_index + 1 :]
        start_index = output_text.find("![`Figure")

    return output_text


def test_simplify_section_headers():
    input_header = '::: {.section type="division" aria-labelledby="sec1"}\n## []{#introduction.xhtml#h-1}`Why I Wrote This Book`{.sample .SANS_Futura_Std_Bold_B_11} {#introduction.xhtml#sec1 .H1}'
    expected_output = "\n## Why I Wrote This Book"

    result = simplify_markdown(input_header)
    assert (
        result == expected_output
    ), f"Test failed: expected '{expected_output}', got '{result}'"


def test_remove_reference_links():
    input_text = (
        "In [[Part II](#part2.xhtml)]{.listplain_Xref}, you'll practice using the CLI."
    )
    expected_output = "In Part II, you'll practice using the CLI."

    result = simplify_markdown(input_text)
    assert (
        result == expected_output
    ), f"Test failed: expected '{expected_output}', got '{result}'"


# Run the tests
test_simplify_section_headers()
test_remove_reference_links()

# Usage example with file input/output
input_file = "book.md"
output_file = "book_simplified.md"

with open(input_file, "r", encoding="utf-8") as file:
    input_content = file.read()

output_content = simplify_markdown(input_content)

with open(output_file, "w", encoding="utf-8") as file:
    file.write(output_content)
