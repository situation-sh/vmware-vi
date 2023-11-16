# UpdateInternetScsiAdvancedOptionsRequestType

The parameters of *HostStorageSystem.UpdateInternetScsiAdvancedOptions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The device of the Internet SCSI HBA adapter.  | 
**target_set** | [**HostInternetScsiHbaTargetSet**](HostInternetScsiHbaTargetSet.md) |  | [optional] 
**options** | [**List[HostInternetScsiHbaParamValue]**](HostInternetScsiHbaParamValue.md) | The list of options to set.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.update_internet_scsi_advanced_options_request_type import UpdateInternetScsiAdvancedOptionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInternetScsiAdvancedOptionsRequestType from a JSON string
update_internet_scsi_advanced_options_request_type_instance = UpdateInternetScsiAdvancedOptionsRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateInternetScsiAdvancedOptionsRequestType.to_json()

# convert the object into a dict
update_internet_scsi_advanced_options_request_type_dict = update_internet_scsi_advanced_options_request_type_instance.to_dict()
# create an instance of UpdateInternetScsiAdvancedOptionsRequestType from a dict
update_internet_scsi_advanced_options_request_type_form_dict = update_internet_scsi_advanced_options_request_type.from_dict(update_internet_scsi_advanced_options_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


