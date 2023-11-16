# HostInternetScsiHbaParamValue

Describes the the value of an iSCSI parameter, and whether the value is being inherited.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_inherited** | **bool** | Indicates if the value is inherited from some other source.  If unset, the value is not inheritable. isInherited can be modified only if it has already been set. If value is to being modified, isInherited should be set to true. Setting isInherited to false will result in the value being once again inherited from the source.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_param_value import HostInternetScsiHbaParamValue

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaParamValue from a JSON string
host_internet_scsi_hba_param_value_instance = HostInternetScsiHbaParamValue.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaParamValue.to_json()

# convert the object into a dict
host_internet_scsi_hba_param_value_dict = host_internet_scsi_hba_param_value_instance.to_dict()
# create an instance of HostInternetScsiHbaParamValue from a dict
host_internet_scsi_hba_param_value_form_dict = host_internet_scsi_hba_param_value.from_dict(host_internet_scsi_hba_param_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


