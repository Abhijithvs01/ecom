document.getElementById("placeOrderBtn").addEventListener("click", () => {

    const firstName = document.getElementById("firstName").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();

    if (!firstName || !email || !phone) {
        alert("Please fill all required fields.");
        return;
    }

    const paymentMethod = document.querySelector(
        'input[name="payment"]:checked'
    ).value;

    alert(
        `Order placed successfully!\n\nCustomer: ${firstName}\nPayment: ${paymentMethod}`
    );

    console.log({
        firstName,
        email,
        phone,
        paymentMethod
    });
});