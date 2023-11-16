# ArrayOfIscsiStatus

A boxed array of *IscsiStatus*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IscsiStatus]**](IscsiStatus.md) |  | 

## Example

```python
from vmware_vi.models.array_of_iscsi_status import ArrayOfIscsiStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIscsiStatus from a JSON string
array_of_iscsi_status_instance = ArrayOfIscsiStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfIscsiStatus.to_json()

# convert the object into a dict
array_of_iscsi_status_dict = array_of_iscsi_status_instance.to_dict()
# create an instance of ArrayOfIscsiStatus from a dict
array_of_iscsi_status_form_dict = array_of_iscsi_status.from_dict(array_of_iscsi_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


