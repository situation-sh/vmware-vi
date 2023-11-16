# FailToEnableSPBM

Fault type that could be thrown when enabling SPBM(Storage Policy Based Management) feature of a compute resource.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cs** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**cs_name** | **str** | The computer resource name  ***Since:*** vSphere API 5.0  | 
**host_license_states** | [**List[ComputeResourceHostSPBMLicenseInfo]**](ComputeResourceHostSPBMLicenseInfo.md) | Array of *ComputeResourceHostSPBMLicenseInfo* that contains SPBM license information for all hosts in the compute resource  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.fail_to_enable_spbm import FailToEnableSPBM

# TODO update the JSON string below
json = "{}"
# create an instance of FailToEnableSPBM from a JSON string
fail_to_enable_spbm_instance = FailToEnableSPBM.from_json(json)
# print the JSON string representation of the object
print FailToEnableSPBM.to_json()

# convert the object into a dict
fail_to_enable_spbm_dict = fail_to_enable_spbm_instance.to_dict()
# create an instance of FailToEnableSPBM from a dict
fail_to_enable_spbm_form_dict = fail_to_enable_spbm.from_dict(fail_to_enable_spbm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


