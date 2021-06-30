install.packages(c("usethis", "devtools", "gridExtra", "rcdk", "tidyverse", "viridis"),
                 INSTALL_opts=c('--no-multiarch'))
options(devtools.install.args = "--no-multiarch")
devtools::install_github("https://github.com/aberHRML/classyfireR")
devtools::install_github("https://github.com/CDK-R/rinchi")
