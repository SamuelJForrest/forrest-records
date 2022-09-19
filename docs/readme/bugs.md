# Bugs

## #1: Basket dropdown scroll icon 

**Bug**
If the user hovers on/off the basket dropdown menu (on desktop), multiple scroll down icons would appear - as a new scroll button was being appended to the menu every time - all with slightly offset animations.

**Fix**
To fix this, I added the following JavaScript logic to remove the scroll button each time the user's mouse leaves the submenu:
```
if (subMenu.length) {
    $(this).hover(function() {
        // reset the basket's scroll position
        basket.scrollTop(0);
        
        // append scroll button is basket dropdown's contents height is greater than basket dropdown's height
        if (subMenuHeight >= 400) {
            basket.append(scrollBtn);
        }
    }, function() {
        // remove scroll button when mouse exits basket dropdown
        $('.scroll').remove();
    });
}
```

**Verdict**: 
After implementing this fix, there is only ever one scroll button present within the basket dropdown - I have deemed this fix successful. A video of the scroll icon can be seen here:

https://user-images.githubusercontent.com/94783808/190649667-eb4d6353-266e-42ad-bd5e-24b55e01170c.mp4

## #2: Bug title

**Bug**: 

**Fix**: 

**Verdict**: 

## Unfixed bugs
- 