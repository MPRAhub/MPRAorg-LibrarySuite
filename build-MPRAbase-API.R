library("devtools")
library("roxygen2")

setwd("/home/jovyan/MPRAhub/MPRAbase")
document()

setwd("../")
usethis::create_package("MPRAbase")