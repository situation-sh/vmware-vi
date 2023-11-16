# LocalizableMessage

Message data which is intended to be displayed according to the locale of a client.  A *LocalizableMessage* contains both a formatted, localized version of the text and the data needed to perform localization in conjunction with localization catalogs.  Clients of the VIM API may use vim.SessionManager.setLocale() to cause the server to emit a localized *LocalizableMessage.message*, or may perform client-side localization based on message catalogs provided by the server. - If the substition variable is a string, no further lookup is required.   - *LocalizableMessage.arg* = \\[(\"address\" = \"127.0.0.1\")\\]   - CATALOG(locmsg, *LocalizableMessage.key*) = \"IP address is {address}\"   - \\==&gt; *LocalizableMessage.message* = \"IP address is 127.0.0.1\" - If the substitution variable is an integer, value is a lookup key.   - *LocalizableMessage.arg* = \\[(\"1\" = \"button.cancel\"), (\"2\" = \"msg.revert\")\\]   - CATALOG(locmsg, *LocalizableMessage.key*) = \"Select '{1}' to {2}\"   - CATALOG(locmsg, button.cancel) = \"Cancel\"   - CATALOG(locmsg, msg.revert) = \"revert\"   - \\==&gt; *LocalizableMessage.message* = \"Select 'Cancel' to revert\" - If the variable contains '@', value is a label lookup in another   catalog, where {name.@CATALOG.prefix} looks up prefix.*LocalizableMessage.arg*\\[name\\].label   in CATALOG.   - *LocalizableMessage.arg* = \\[(\"field\" = \"queued\")\\]   - CATALOG(locmsg, *LocalizableMessage.key*) = \"State is {field.@enum.TaskInfo.State}\"   - CATALOG(enum, TaskInfo.State.queued.label) is \"Queued\"   - \\==&gt; *LocalizableMessage.message* = \"State is Queued\"      ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Unique key identifying the message in the localized message catalog.  ***Since:*** vSphere API 4.0  | 
**arg** | [**List[KeyAnyValue]**](KeyAnyValue.md) | Substitution arguments for variables in the localized message.  ***Since:*** vSphere API 4.0  | [optional] 
**message** | **str** | Message in session locale.  Use vim.SessionManager.setLocale() to change the session locale.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.localizable_message import LocalizableMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizableMessage from a JSON string
localizable_message_instance = LocalizableMessage.from_json(json)
# print the JSON string representation of the object
print LocalizableMessage.to_json()

# convert the object into a dict
localizable_message_dict = localizable_message_instance.to_dict()
# create an instance of LocalizableMessage from a dict
localizable_message_form_dict = localizable_message.from_dict(localizable_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


