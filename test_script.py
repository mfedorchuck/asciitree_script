import tree_builder

message = "(asciitree(sometimes you)(just(want to draw)) trees (in(your terminal)))"
long_message = "(asciitree(sometimes you)(just(want to draw)) trees with (deep(deep(deep(branches)))) (in(your terminal)))"
bad_message = "this is not asciitree format"
bad_message_2 = "(this is not (asciitree correct format)"

checked_message = tree_builder.check_layout(message)

message_structure = tree_builder.build_structure(checked_message)
tree_builder.print_structure(message_structure)
