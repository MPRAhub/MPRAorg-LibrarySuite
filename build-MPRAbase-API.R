library("devtools")
library("roxygen2")
library("usethis")

setwd("/home/jovyan/MPRAhub/MPRAbase")
document()

setwd("../")
options(usethis.ask.default = FALSE)
devtools::install("MPRAbase")
