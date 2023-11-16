# ArrayOfHostInternetScsiHbaAuthenticationProperties

A boxed array of *HostInternetScsiHbaAuthenticationProperties*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostInternetScsiHbaAuthenticationProperties]**](HostInternetScsiHbaAuthenticationProperties.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_internet_scsi_hba_authentication_properties import ArrayOfHostInternetScsiHbaAuthenticationProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostInternetScsiHbaAuthenticationProperties from a JSON string
array_of_host_internet_scsi_hba_authentication_properties_instance = ArrayOfHostInternetScsiHbaAuthenticationProperties.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostInternetScsiHbaAuthenticationProperties.to_json()

# convert the object into a dict
array_of_host_internet_scsi_hba_authentication_properties_dict = array_of_host_internet_scsi_hba_authentication_properties_instance.to_dict()
# create an instance of ArrayOfHostInternetScsiHbaAuthenticationProperties from a dict
array_of_host_internet_scsi_hba_authentication_properties_form_dict = array_of_host_internet_scsi_hba_authentication_properties.from_dict(array_of_host_internet_scsi_hba_authentication_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


