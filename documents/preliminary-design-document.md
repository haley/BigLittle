# Preliminary Database Design Document

## 1.1 Project Description


This project is to support a future 402 project. The project on a greater scale is to create a website to help people pair up mentors and mentees in college environments. In many student organizations there are “bigs” and “littles,” that pair up new members with more experience members. The project’s goal is to create a web service where social chairs of organizations are able to invite people in their organizations to input their preferences for both potential bigs and potential littles. The database would be used to store information on both bigs and littles as well as their preferences, emails, and eventually who they have been matched with. In addition to this the database will store the information for “tentative engagements” which are a necessary part of the big-little matching algorithm. We plan to use MongoDB.

## 1.2 Data Description


The data that will be stored in the Big-Little database include:

* Information on people: userIds, emails, whether they are a big or a little, which match process Id(s) they are associated with, etc.
* Information on preferences: Which order different users prefer other users in
* Information on match processes: Who the organizer is, which users are part of the match process, specifications about the match process
* Information on “Engagements”: Part of the algorithm involves the matches being temporarily ‘engaged’ and then once every user has a match these ‘engagements’ become finalized and everyone has a match. This would store userIds of pairs that are ‘engaged.’

## 1.3 Examples


* *Organizer* could find out the final list of matches of their org

* *Organizer* could find out the user information of the members of their org
* *Organizer* could find out which members of their org have filled out their preferences
* *Organizer* could get a full list of members in their org
* *Organizer* could get a full list of engagements in their org
* *User* can see their own user information as well as their memberships
* *Members* can see all members that they are engaged to, as well as their user information

## 1.4 Schema of the database

**User** - people that will interact with the database

| Attribute    | Type |
| --------------- | ---- |
| ID | int |
| Name        |   string   |
| Email       | string |
| PhoneNumber | string |
| Year        | int |
| BirthDate   | date |

**Organization** - group of members with a collective name and societal type

| Attribute | Type   |
| --------- | ------ |
| ID        | int    |
| Name      | string |
| Type      | string |

**Member** - membership of an organization for a user

| Attribute  | Type   |
| ---------- | ------ |
| ID         | int    |
| UserID     | int    |
| OrgID      | int    |
| RoleName   | string |
| DateJoined | date   |

**Preferred** - member's preferences for other members for engagements

| Attribute         | Type |
| ----------------- | ---- |
| ID                | int  |
| MemberID          | int  |
| PreferredMemberID | int  |

**Engaged** - paired matching of two members (mentor - mentee relationship)

| Attribute      | Type |
| -------------- | ---- |
| ID             | int  |
| MenteeMemberID | int  |
| MentorMemberID | int  |

## Preliminary Entity Relation Diagram

![ERD](resources/ERD.png)
