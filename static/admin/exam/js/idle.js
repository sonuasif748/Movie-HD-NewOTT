       // Set timeout variables.
var timoutWarning = 600000; // Display warning in 14 Mins.
var timoutNow = 600000; // Timeout in 15 mins.
var logoutUrl = 'ct3.gitam.edu'; // URL to logout page.

var warningTimer;
var timeoutTimer;

// Start timers.
function StartTimers() {
    //warningTimer = setTimeout("IdleWarning()", timoutWarning);
    timeoutTimer = setTimeout("IdleTimeout()", timoutNow);
}

// Reset timers.
function ResetTimers() {
    clearTimeout(warningTimer);
    clearTimeout(timeoutTimer);
    StartTimers();
    //$("#timeout").dialog('close');
}

// Show idle timeout warning dialog.
function IdleWarning() {
    // $("#timeout").dialog({
    //     modal: true
    // });
}

// Logout the user.
function IdleTimeout() {
    //alert('You are idle from last 10 minutes so your exam has been considered as absent')
    $("#submit_type").val('5');
    $('#modal_form').submit();
    //window.location = logoutUrl;
}