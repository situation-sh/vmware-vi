# OvfValidateHostResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_size** | **int** | The total amount of data that must be transferred to download the entity.  This may be inaccurate due to disk compression etc.  ***Since:*** vSphere API 4.0  | [optional] 
**flat_deployment_size** | **int** | The total amount of space required to deploy the entity if using flat disks.  ***Since:*** vSphere API 4.0  | [optional] 
**sparse_deployment_size** | **int** | The total amount of space required to deploy the entity using sparse disks, if known.  ***Since:*** vSphere API 4.0  | [optional] 
**error** | [**List[MethodFault]**](MethodFault.md) | Errors that happened during validation.  The presence of faults in this list indicates that the validation failed.  ***Since:*** vSphere API 4.0  | [optional] 
**warning** | [**List[MethodFault]**](MethodFault.md) | Non-fatal warnings from the validation.  ***Since:*** vSphere API 4.0  | [optional] 
**supported_disk_provisioning** | **List[str]** | An array of the disk provisioning type supported by the target host system.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.ovf_validate_host_result import OvfValidateHostResult

# TODO update the JSON string below
json = "{}"
# create an instance of OvfValidateHostResult from a JSON string
ovf_validate_host_result_instance = OvfValidateHostResult.from_json(json)
# print the JSON string representation of the object
print OvfValidateHostResult.to_json()

# convert the object into a dict
ovf_validate_host_result_dict = ovf_validate_host_result_instance.to_dict()
# create an instance of OvfValidateHostResult from a dict
ovf_validate_host_result_form_dict = ovf_validate_host_result.from_dict(ovf_validate_host_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


