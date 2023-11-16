# ArrayOfVimAccountPasswordChangedEvent

A boxed array of *VimAccountPasswordChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VimAccountPasswordChangedEvent]**](VimAccountPasswordChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vim_account_password_changed_event import ArrayOfVimAccountPasswordChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVimAccountPasswordChangedEvent from a JSON string
array_of_vim_account_password_changed_event_instance = ArrayOfVimAccountPasswordChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVimAccountPasswordChangedEvent.to_json()

# convert the object into a dict
array_of_vim_account_password_changed_event_dict = array_of_vim_account_password_changed_event_instance.to_dict()
# create an instance of ArrayOfVimAccountPasswordChangedEvent from a dict
array_of_vim_account_password_changed_event_form_dict = array_of_vim_account_password_changed_event.from_dict(array_of_vim_account_password_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


