# QueryVsanUpgradeStatusRequestType

The parameters of *VsanUpgradeSystem.QueryVsanUpgradeStatus*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_vsan_upgrade_status_request_type import QueryVsanUpgradeStatusRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVsanUpgradeStatusRequestType from a JSON string
query_vsan_upgrade_status_request_type_instance = QueryVsanUpgradeStatusRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVsanUpgradeStatusRequestType.to_json()

# convert the object into a dict
query_vsan_upgrade_status_request_type_dict = query_vsan_upgrade_status_request_type_instance.to_dict()
# create an instance of QueryVsanUpgradeStatusRequestType from a dict
query_vsan_upgrade_status_request_type_form_dict = query_vsan_upgrade_status_request_type.from_dict(query_vsan_upgrade_status_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


