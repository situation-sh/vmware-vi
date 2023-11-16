# EVCAdmissionFailedCPUModel

The host's CPU hardware is a family/model that does not support any Enhanced VMotion Compatibility mode.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.evc_admission_failed_cpu_model import EVCAdmissionFailedCPUModel

# TODO update the JSON string below
json = "{}"
# create an instance of EVCAdmissionFailedCPUModel from a JSON string
evc_admission_failed_cpu_model_instance = EVCAdmissionFailedCPUModel.from_json(json)
# print the JSON string representation of the object
print EVCAdmissionFailedCPUModel.to_json()

# convert the object into a dict
evc_admission_failed_cpu_model_dict = evc_admission_failed_cpu_model_instance.to_dict()
# create an instance of EVCAdmissionFailedCPUModel from a dict
evc_admission_failed_cpu_model_form_dict = evc_admission_failed_cpu_model.from_dict(evc_admission_failed_cpu_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


