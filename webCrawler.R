
install.packages('rvest')
install.packages('stringr')

library(stringr)
library(rvest)



count_word_occurrences <- function(url, word) {
  source_code <- read_html(url)
  text <- str_to_lower(html_text(source_code))
  word_count <- str_count(text, fixed(word, ignore_case = TRUE))
  return(word_count)
}

url <- 'https://en.wikipedia.org/wiki/John_von_Neumann'  # selected web page
word <- 'math'  # target word
word_count <- count_word_occurrences(url, word)
cat(paste0('The word "', word, '" occurs ', word_count, ' times on the page.')) 
