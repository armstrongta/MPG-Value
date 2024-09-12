from shiny import ui, render, App
# Run Shiny, but exclude the reload statements:
# & 'c:\Users\18015\OneDrive\repo\mpg value\.conda\python.exe' -m shiny run --port 51239 'c:\Users\18015\OneDrive\repo\mpg value\app.py'


app_ui = ui.page_fillable(
    ui.h1("Fuel Cost Comparison App"),
    ui.layout_columns(
    ui.card(ui.input_slider("year_miles", "Miles Driven in 1 year", 0, 50000, 20000, step = 2000, post = " miles"), 
    ui.input_slider("years", "Years of Driving with this car", 0, 40, 5, post = " years"),
    ui.div(
        "Average $ per Gallon",
        ui.HTML("<div style='line-height: 0.8em;'><small style='font-size: 12px;'>(over the above time frame)</small></div><br>"),
        ui.input_slider("cost_per_gal", "", 2, 6, 3.5, step=0.25, pre="$"),
    )),
    ui.card(ui.input_slider("mpg1", "Miles Per Gallon car 1", 5, 40, 22, post=" mpg"),
    ui.input_slider("mpg2", "Miles Per Gallon car 2", 5, 40, 24, post = " mpg")), 
    ui.card(ui.output_text_verbatim("calc_cost"),
    ui.HTML('''
        <div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="https://giphy.com/embed/oBf40z4p7QNCz0y3mT" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/RollzInternational-fun-movie-trailer-oBf40z4p7QNCz0y3mT"></a></p>
    ''')),
    col_widths=(3,3,4),

),)

def server(input, output, session):
    @output
    @render.text
    def calc_cost():
        year_miles= input.year_miles()
        years=input.years()
        mpg1=input.mpg1()
        mpg2=input.mpg2()
        cost_per_gal=input.cost_per_gal()

        total_miles = years * year_miles
        gallons1 = total_miles / mpg1
        cost1 = gallons1 * cost_per_gal

        gallons2 = total_miles / mpg2
        cost2 = gallons2 * cost_per_gal

        better_car = (lambda cost1, cost2: "Car 1" if cost1 < cost2 else "Car 2")(cost1, cost2)
        savings = abs(cost2 - cost1)

        return (
            f"Car 1 gas money in {years} years: ${cost1:,.2f}\n"
            f"Car 2 gas money in {years} years: ${cost2:,.2f}\n"
            f"\nYou will save ${savings:,.2f} by choosing {better_car}!"
        )

app = App(app_ui, server)