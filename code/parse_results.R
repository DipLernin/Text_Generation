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
  # for (j in 1:length(grep("Iteration", text))) {
  for (j in 1:20) {
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

res_poetry <- parse_output("../expriments/poems_default.txt")
res_marvel <- parse_output("../expriments/marvel_default.txt")
res_odyssey <- parse_output("../expriments/odessy_default.txt")
res_darwin <- parse_output("../expriments/darwin_default.txt")


# summary plot
jpeg(file = "../plots/plot_all.jpg")

plot(res_darwin$Iteration, res_darwin$loss, xlab = "Epoch", ylab = "Loss", 
     main = "Epochs vs Loss", pch = 20, col = "seagreen")
lines(res_darwin$Iteration, res_darwin$loss, col = "seagreen")

points(res_odyssey$Iteration, res_odyssey$loss, pch = 20, col = "maroon1")
lines(res_odyssey$Iteration, res_odyssey$loss, col = "maroon1")

points(res_poetry$Iteration, res_poetry$loss, pch = 20, col = "red")
lines(res_poetry$Iteration, res_poetry$loss, col = "red")

points(res_marvel$Iteration, res_marvel$loss, pch = 20, col = "blue")
lines(res_marvel$Iteration, res_marvel$loss, col = "blue")

legend("topright", title="Data", cex=1.25,
       c("Marvel train", "Poetry train", 
        "Odyssey train", "Darwin train"), 
       fill=c("blue", "red", 
              "maroon1", "seagreen"))

dev.off()

jpeg(file = "../plots/darwin_plot.jpg")

plot(res_darwin$Iteration, res_darwin$loss, xlab = "Epoch", ylab = "Loss", 
     main = "Darwin text", pch = 20, col = "seagreen")
lines(res_darwin$Iteration, res_darwin$loss, col = "seagreen")

points(res_darwin$Iteration, res_darwin$val_loss, pch = 20, col = "seagreen1")
lines(res_darwin$Iteration, res_darwin$val_loss, col = "seagreen1")

legend("topright", title="Data",  cex=1.25,
       c("Train",  "Test"), 
       fill=c("seagreen", "seagreen1"))

dev.off()

jpeg(file = "../plots/odyssey_plot.jpg")

plot(res_odyssey$Iteration, res_odyssey$loss, xlab = "Epoch", ylab = "Loss", 
       main = "Odyssey text", pch = 20, col = "purple4")
lines(res_odyssey$Iteration, res_odyssey$loss, col = "purple4")

points(res_odyssey$Iteration, res_odyssey$val_loss, pch = 20, col = "plum")
lines(res_odyssey$Iteration, res_odyssey$val_loss, col = "plum")

legend("topright", title="Data",  cex=1.25,
       c("Train",  "Test"), 
       fill=c("purple4", "plum"))

dev.off()


jpeg(file = "../plots/poetry_plot.jpg")

plot(res_poetry$Iteration, res_poetry$loss, xlab = "Epoch", ylab = "Loss", 
       main = "Poetry text",, pch = 20, col = "red")
lines(res_poetry$Iteration, res_poetry$loss, col = "red")

points(res_poetry$Iteration, res_poetry$val_loss, pch = 20, col = "pink")
lines(res_poetry$Iteration, res_poetry$val_loss, col = "pink")

legend("topright", title="Data",  cex=1.25,
       c("Train",  "Test"), 
       fill=c("red", "pink"))

dev.off()


jpeg(file = "../plots/marvel_plot.jpg")

plot(res_marvel$Iteration, res_marvel$loss, xlab = "Epoch", ylab = "Loss", 
       main = "Marvel text", pch = 20, col = "blue")
lines(res_marvel$Iteration, res_marvel$loss, col = "blue")

points(res_marvel$Iteration, res_marvel$val_loss, pch = 20, col = "turquoise")
lines(res_marvel$Iteration, res_marvel$val_loss, col = "turquoise")

legend("topright", title="Data", cex=1.25,
       c("Train",  "Test"), 
       fill=c("blue", "turquoise"))

dev.off()
