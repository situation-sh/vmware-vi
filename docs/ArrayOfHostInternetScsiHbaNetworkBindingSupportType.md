# ArrayOfHostInternetScsiHbaNetworkBindingSupportType

A boxed array of *HostInternetScsiHbaNetworkBindingSupportType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostInternetScsiHbaNetworkBindingSupportTypeEnum]**](HostInternetScsiHbaNetworkBindingSupportTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_internet_scsi_hba_network_binding_support_type import ArrayOfHostInternetScsiHbaNetworkBindingSupportType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostInternetScsiHbaNetworkBindingSupportType from a JSON string
array_of_host_internet_scsi_hba_network_binding_support_type_instance = ArrayOfHostInternetScsiHbaNetworkBindingSupportType.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostInternetScsiHbaNetworkBindingSupportType.to_json()

# convert the object into a dict
array_of_host_internet_scsi_hba_network_binding_support_type_dict = array_of_host_internet_scsi_hba_network_binding_support_type_instance.to_dict()
# create an instance of ArrayOfHostInternetScsiHbaNetworkBindingSupportType from a dict
array_of_host_internet_scsi_hba_network_binding_support_type_form_dict = array_of_host_internet_scsi_hba_network_binding_support_type.from_dict(array_of_host_internet_scsi_hba_network_binding_support_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


