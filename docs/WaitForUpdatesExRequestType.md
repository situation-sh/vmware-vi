# WaitForUpdatesExRequestType

The parameters of *PropertyCollector.WaitForUpdatesEx*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The data version currently known to the client. The value must be either - the special initial data version (an empty string), - a data version returned from *PropertyCollector.CheckForUpdates* or *PropertyCollector.WaitForUpdates* - a non-truncated data version returned from *PropertyCollector.WaitForUpdatesEx* - a truncated data version returned from the last call to *PropertyCollector.WaitForUpdatesEx* with no intervening calls to *PropertyCollector.WaitForUpdates* or *PropertyCollector.CheckForUpdates*.  | [optional] 
**options** | [**WaitOptions**](WaitOptions.md) |  | [optional] 

## Example

```python
from vmware_vi.models.wait_for_updates_ex_request_type import WaitForUpdatesExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of WaitForUpdatesExRequestType from a JSON string
wait_for_updates_ex_request_type_instance = WaitForUpdatesExRequestType.from_json(json)
# print the JSON string representation of the object
print WaitForUpdatesExRequestType.to_json()

# convert the object into a dict
wait_for_updates_ex_request_type_dict = wait_for_updates_ex_request_type_instance.to_dict()
# create an instance of WaitForUpdatesExRequestType from a dict
wait_for_updates_ex_request_type_form_dict = wait_for_updates_ex_request_type.from_dict(wait_for_updates_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


