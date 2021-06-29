from domdf_python_tools.paths import PathPlus


def replace_unicode(app, exception):
	if exception:
		return

	if app.builder.name.lower() != "latex":
		return

	output_file = PathPlus(app.builder.outdir) / f"{app.builder.titles[0][1]}.tex"

	output_content = output_file.read_text()
	output_content = output_content.replace('➞', r" $\rightarrow$ ")
	output_file.write_clean(output_content)


def setup(app):
	app.connect("build-finished", replace_unicode)
