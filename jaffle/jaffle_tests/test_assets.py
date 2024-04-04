
from jaffle.assets import population, continent_population
from jaffle.duckpond import DuckDb


def test_assests():
    p = population()
    c = continent_population(p)

    assert(
        c.sql 
        =="select continent, avg(pop_change) as avg_pop_change from $population group by 1 order by 2 desc"
    )
    assert "population" in c.bindings
    df = DuckDb().query(c)
    top = df.loc[0]
    assert top["continent"] == "Africa"
    assert round(top["avg_pop_change"]) == 2