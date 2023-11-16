# VimAccountPasswordChangedEvent

Password for the Vim account user on the host has been changed.  This is an account created by VirtualCenter and used to manage the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vim_account_password_changed_event import VimAccountPasswordChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VimAccountPasswordChangedEvent from a JSON string
vim_account_password_changed_event_instance = VimAccountPasswordChangedEvent.from_json(json)
# print the JSON string representation of the object
print VimAccountPasswordChangedEvent.to_json()

# convert the object into a dict
vim_account_password_changed_event_dict = vim_account_password_changed_event_instance.to_dict()
# create an instance of VimAccountPasswordChangedEvent from a dict
vim_account_password_changed_event_form_dict = vim_account_password_changed_event.from_dict(vim_account_password_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


