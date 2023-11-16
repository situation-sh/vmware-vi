# InitializeDisksRequestType

The parameters of *HostVsanSystem.InitializeDisks_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**List[VsanHostDiskMapping]**](VsanHostDiskMapping.md) | list of disk mappings to initialize  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.initialize_disks_request_type import InitializeDisksRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InitializeDisksRequestType from a JSON string
initialize_disks_request_type_instance = InitializeDisksRequestType.from_json(json)
# print the JSON string representation of the object
print InitializeDisksRequestType.to_json()

# convert the object into a dict
initialize_disks_request_type_dict = initialize_disks_request_type_instance.to_dict()
# create an instance of InitializeDisksRequestType from a dict
initialize_disks_request_type_form_dict = initialize_disks_request_type.from_dict(initialize_disks_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


