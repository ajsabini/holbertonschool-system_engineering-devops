# 0x19 Postmorten

## Issue summary

    - duration
        Start at 08/14/2022 14:54 UTC-3
    - user experience
        can't acess toany data provide from database, 100% of users were affected
    - root cause
        updating php version

# Timeline
   
    the issue was detected at 08/14/2022 14:54 for the administrator ofthe website, 
    and a few minutes later several users complained about the failure. First action
    we taken was put all the website under maintenance. We escalate the issue to our
    support team and open a ticket with the hosting provider. Finally we foud the
    origin of issue, the php version was updated, and the sql queries was deprecated

## Root cause and resolution
  
    Pulling the thread we found that the developer team install a new php library for
    convert html to pdf, and one of the requeriments was the php version must be
    7 or greater, and update the php version and affet some oldest scripts, that 
    php mark as obsolet.
    
    To fix the problem we had to rewrite all database queries with the new php 
    implementation.

## Corrective and preventative measures

    To prevent this from happening again, the development team must be extremely 
    attentive to the fact that any update of any component of the server can generate 
    some kind of problem, so the first step before making an update is to make a 
    backup, to know if it allows to revert that update in case it starts to fail, to 
    check beforehand what can fail if an update is made.
