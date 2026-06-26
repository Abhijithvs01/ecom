let plusButtons = document.querySelectorAll(".plus");
let minusButtons = document.querySelectorAll(".minus");

plusButtons.forEach(function(button){

    button.addEventListener("click", function(){

        let input = this.parentElement.querySelector(".qty-input");

        let value = parseInt(input.value);

        input.value = value + 1;

    });

});

minusButtons.forEach(function(button){

    button.addEventListener("click", function(){

        let input = this.parentElement.querySelector(".qty-input");

        let value = parseInt(input.value);

        if(value > 1){
            input.value = value - 1;
        }

    });

});