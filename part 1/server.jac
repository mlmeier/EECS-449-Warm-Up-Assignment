walker interact {
    can return_message with `root entry {
        report {
            "response": "Hello, world!"
        };
    }
}

walker interact_with_body {
    has name: str;

    can return_message with `root entry {
        report {
            "response": "Hello, " + self.name + "!"
        };
    }
}

walker simple_calculator {
    has num1: float;
    has num2: float;
    can add_numbers with `root entry {
        
        report {
            "response": "The sum is " + str(self.num1 + self.num2) + "."
        };
    }


}
walker number_checker {
    has number: int;
    
    can check_number with `root entry {
        if self.number >= 100 {
            report {
                "response": "Number greater than or equal to 100."
            };
        } else {
            report {
                "response": "Number less than 100."
            };
        }
    }
}