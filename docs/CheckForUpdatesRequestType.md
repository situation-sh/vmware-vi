# CheckForUpdatesRequestType

The parameters of *PropertyCollector.CheckForUpdates*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The data version currently known to the client. The value must be either - the special initial version (an empty string) - a data version returned from *PropertyCollector.CheckForUpdates* or *PropertyCollector.WaitForUpdates* by the same *PropertyCollector* on the same session. - a non-truncated data version returned from *PropertyCollector.WaitForUpdatesEx* by the same *PropertyCollector* on the same   session.  | [optional] 

## Example

```python
from vmware_vi.models.check_for_updates_request_type import CheckForUpdatesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckForUpdatesRequestType from a JSON string
check_for_updates_request_type_instance = CheckForUpdatesRequestType.from_json(json)
# print the JSON string representation of the object
print CheckForUpdatesRequestType.to_json()

# convert the object into a dict
check_for_updates_request_type_dict = check_for_updates_request_type_instance.to_dict()
# create an instance of CheckForUpdatesRequestType from a dict
check_for_updates_request_type_form_dict = check_for_updates_request_type.from_dict(check_for_updates_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


