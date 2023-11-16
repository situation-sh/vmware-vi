# EventDescriptionEventDetail

Each Event object provides an automatic event message string through its *fullFormattedMessage* property.  However, you can use the EventDetail object's properties to format an event message string that is appropriate when viewed from a specific context. The variable information (vm.name, and so on) is derived from the Event object's event arguments (*VmEventArgument*, and so on). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Type of event being described.  | 
**description** | **str** | A string that is a short human-parseable description of the event.  This is not the full message string (which may contain details of the arguments, etc.), but merely a more understandable, and localized, description of what the event stands for. It is meant for contexts where the _name_ of the event has to be displayed to end-users, e.g. when creating Event-based Alarms. \\&#x60; \\*   E.g., for *VmPoweredOnEvent*, the eventDescription in English might say \&quot;VM Powered On\&quot;.  ***Since:*** vSphere API 4.0  | [optional] 
**category** | **str** | A category of events.  | 
**format_on_datacenter** | **str** | A string that is appropriate in the context of a specific Datacenter.  For example, a renaming event in this context produces the following string:  \&quot;Renamed {vm.name} from {oldName} to {newName}\&quot;  where *oldName* and *newName* are properties of the VmRenamedEvent object.  | 
**format_on_compute_resource** | **str** | A string that is appropriate in the context of a specific cluster.  For example, a powering on event in this context produces the following string:  \&quot;{vm.name} on {host.name} is powered on\&quot;.  | 
**format_on_host** | **str** | A string that is appropriate in the context of a specific Host.  For example, a powering on event in this context produces the following string:  \&quot;{vm.name} is powered on\&quot;  | 
**format_on_vm** | **str** | A string that is appropriate for the context of a specific virtual machine.  For example, a powering on event in this context produces the following string:  \&quot;Virtual machine on {host.name} is powered on\&quot;  | 
**full_format** | **str** | A string whose context is not entity-specific.  For example, a powering on event produces the following string:  \&quot;{vm.name} on {host.name} in {datacenter.name} is powered on\&quot;  | 
**long_description** | **str** | A detailed description of the event.  It includes common causes and actions to remediate them. It may also include links to kb articles and other diagnostic information. For example, the BadUserNameSessionEvent may produce the following string:           &lt;EventLongDescription id&#x3D;\&quot;vim.event.BadUserNameSessionEvent\&quot;&gt;             &lt;description&gt;                The user could not be logged in because of an unknown or invalid                user name.             &lt;/description&gt;             &lt;cause&gt;                &lt;description&gt;The user name was unknown to the system&lt;/description&gt;                &lt;action&gt;Use a user name known to the system user directory&lt;/action&gt;                &lt;action&gt;(On Linux) Check if the user directory is correctly                        configured.&lt;/action&gt;                &lt;action&gt;Check the health of the domain controller (if you are using                        Active Directory)&lt;/action&gt;             &lt;/cause&gt;             &lt;cause&gt;                &lt;description&gt;The user provided an invalid password&lt;/description&gt;                &lt;action&gt;Supply the correct password&lt;/action&gt;             &lt;/cause&gt;          &lt;/EventLongDescription&gt;  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.event_description_event_detail import EventDescriptionEventDetail

# TODO update the JSON string below
json = "{}"
# create an instance of EventDescriptionEventDetail from a JSON string
event_description_event_detail_instance = EventDescriptionEventDetail.from_json(json)
# print the JSON string representation of the object
print EventDescriptionEventDetail.to_json()

# convert the object into a dict
event_description_event_detail_dict = event_description_event_detail_instance.to_dict()
# create an instance of EventDescriptionEventDetail from a dict
event_description_event_detail_form_dict = event_description_event_detail.from_dict(event_description_event_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


