
// Simple smooth scroll for better UX (can expand with more features later)
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('predictForm');
    if(form){
        form.addEventListener('submit', function(){
            window.scrollTo({top: 0, behavior: 'smooth'});
        });
    }
});
