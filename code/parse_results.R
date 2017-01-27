# taking the evaluation metrics values
parse_line <- function(row) {
  list <- unlist(strsplit(row, " "))
  return(list[c(7,10,13,16)])
}

# parsing the whole output file
parse_output <- function(filename) {
  text <- readLines(filename, encoding = "UTF-8")
  # if the output is corrupted- we only care of the part that starts with "Build model"
  for (i in 1:length(text)) {
    if (text[i]=="Build model...") {
      text <- text[i:length(text)]
      break
    }
  }
  result_data <- as.data.frame(matrix(nrow = 0, ncol = 2))
  # first line that says "Iteration" is line 5, and the next ones are i+4
  i <- 5
  # for the number of iterations in the output
  for (j in 1:length(grep("Iteration", text))) {
    result_data[j,] <- c(text[i], text[i-1])
    i <- i+4
  }
  
  result_data <- cbind(result_data, as.data.frame(t(sapply(result_data$V2, parse_line))))
  result_data$V2 <- NULL
  colnames(result_data) <- c("Iteration", "loss", "acc", "val_loss", "val_acc")
  result_data$Iteration <- gsub("Iteration ", "", result_data$Iteration)
  result_data <- sapply(result_data, function(x) as.numeric(as.character(x)))
  return(as.data.frame(result_data))
}

res_poetry <- parse_output("../datasets/poems_default.txt")
res_marvel <- parse_output("../datasets/marvel_default.txt")


# training plot
jpeg(file = "../plots/train_plot.jpg")

plot(res_poetry$acc, res_poetry$loss, xlab = "Accuracy", ylab = "Loss", 
     main = "Train Loss vs Accuracy", pch = 20, col = "red")
lines(res_poetry$acc, res_poetry$loss, col = "red")

points(res_marvel$acc, res_marvel$loss, pch = 20, col = "blue")
lines(res_marvel$acc, res_marvel$loss, col = "blue")

legend("topright", title="Data", 
       c("Poetry","Marvel movies"), fill=c("red", "blue"))

dev.off()

# validation plot

jpeg(file = "../plots/valid_plot.jpg")

plot(res_poetry$val_acc, res_poetry$val_loss, xlab = "Accuracy", ylab = "Loss", 
     main = "Validation Loss vs Accuracy", pch = 20, col = "green")
lines(res_poetry$val_acc, res_poetry$val_loss, col = "green")

points(res_marvel$val_acc, res_marvel$val_loss, pch = 20, col = "purple")
lines(res_marvel$val_acc, res_marvel$val_loss, col = "purple")

legend("topright", title="Data",
       c("Poetry","Marvel movies"), fill=c("green", "purple"))

dev.off()
