# VirtualMachineMessage

Message data which is intended to be displayed according to the locale of a client.  A *VirtualMachineMessage* contains both a formatted, localized version of the text and the data needed to perform localization in conjunction with localization catalogs.  Clients of the VIM API may use *SessionManager*.*SessionManager.SetLocale* to cause the server to emit localized *VirtualMachineMessage.text*, or may perform client-side localization based on message catalogs provided by the *LocalizationManager*.  Message variables are always integers, e.g. {1} and {2}, which are 1-based indexes into *VirtualMachineMessage.argument*. - The corresponding argument may be a recursive lookup:   - *VirtualMachineMessage.argument* = \\[\"button.cancel\", \"msg.revert\"\\]   - CATALOG(locmsg, *VirtualMachineMessage.id*) = \"Select '{1}' to {2}\"   - CATALOG(locmsg, button.cancel) = \"Cancel\"   - CATALOG(locmsg, msg.revert) = \"revert\"   - \\==&gt; *VirtualMachineMessage.text* = \"Select 'Cancel' to revert\" - If the recursive lookup fails, the argument is a plain string.   - *VirtualMachineMessage.argument* = \\[\"127.0.0.1\"\\]   - CATALOG(locmsg, *VirtualMachineMessage.id*) = \"IP address is {1}\"   - \\==&gt; *VirtualMachineMessage.text* \"IP address is 127.0.0.1\"      See also *LocalizationManager*.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for this particular message.  This field is a key for looking up format strings in the locmsg catalog.  ***Since:*** VI API 2.5  | 
**argument** | [**List[Any]**](Any.md) | Substitution arguments for variables in the localized message.  Substitution variables in the format string identified by *VirtualMachineMessage.id* are 1-based indexes into this array. Substitution variable {1} corresponds to argument\\[0\\], etc.  ***Since:*** VI API 2.5  | [optional] 
**text** | **str** | Text in session locale.  Use *SessionManager*.*SessionManager.SetLocale* to change the session locale.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_message import VirtualMachineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMessage from a JSON string
virtual_machine_message_instance = VirtualMachineMessage.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMessage.to_json()

# convert the object into a dict
virtual_machine_message_dict = virtual_machine_message_instance.to_dict()
# create an instance of VirtualMachineMessage from a dict
virtual_machine_message_form_dict = virtual_machine_message.from_dict(virtual_machine_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


