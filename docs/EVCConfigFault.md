# EVCConfigFault

An attempt to enable Enhanced VMotion Compatibility on a cluster has failed.  ***Since:*** VI API 2.5u2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faults** | [**List[MethodFault]**](MethodFault.md) | The faults that caused this EVC test to fail, such as *FeatureRequirementsNotMet* faults.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.evc_config_fault import EVCConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of EVCConfigFault from a JSON string
evc_config_fault_instance = EVCConfigFault.from_json(json)
# print the JSON string representation of the object
print EVCConfigFault.to_json()

# convert the object into a dict
evc_config_fault_dict = evc_config_fault_instance.to_dict()
# create an instance of EVCConfigFault from a dict
evc_config_fault_form_dict = evc_config_fault.from_dict(evc_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


