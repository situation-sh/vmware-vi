# LatencySensitivity

Specification of the latency-sensitivity information.  The latency-sensitivity is used to request from the kernel a constraint on the scheduling delay of the virtual CPUs or other resources. This allows latency-sensitive applications(e.g. VOIP, audio/video streaming, etc.) to run in a virtual machine which is configured to use specific scheduling latencies and to be scheduled with low latency.  The kernel does not provide any guarantee that it will meet the latency-sensitivity requirement of a virtual machine CPU or other resources but it will always accept the latency-sensitivity value provided.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**LatencySensitivitySensitivityLevelEnum**](LatencySensitivitySensitivityLevelEnum.md) |  | 
**sensitivity** | **int** | Deprecated as of vSphere version 5.5, this field is deprecated.  The custom absolute latency-sensitivity value of the application.  This value will be used only when the latency-sensitivity *LatencySensitivity.level* property is is set to &lt;code&gt;custom&lt;/code&gt;. It is ignored in all other cases.  The unit of this value is micro-seconds and the application is more latency sensitive when this value is smaller. For example, if the absolute latency-sensitivity is 2000us, the kernel will try to schedule the virtual machine in a way so that its scheduling latency is not more than 2ms.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.latency_sensitivity import LatencySensitivity

# TODO update the JSON string below
json = "{}"
# create an instance of LatencySensitivity from a JSON string
latency_sensitivity_instance = LatencySensitivity.from_json(json)
# print the JSON string representation of the object
print LatencySensitivity.to_json()

# convert the object into a dict
latency_sensitivity_dict = latency_sensitivity_instance.to_dict()
# create an instance of LatencySensitivity from a dict
latency_sensitivity_form_dict = latency_sensitivity.from_dict(latency_sensitivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


