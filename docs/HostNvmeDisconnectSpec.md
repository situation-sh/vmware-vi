# HostNvmeDisconnectSpec

Specifies the parameters necessary to disconnect an NVME controller from a given NVME over Fabrics adapter.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hba_name** | **str** | The device name of the NVME over Fabrics host bus adapter.  ***Since:*** vSphere API 7.0  | 
**subnqn** | **str** | NVME Qualified Name of the NVM subsystem to disconnect from.  If controllerNumber is not specified, the subsystem qualified name has to be specified and any controllers exposed by that subsystem will be disconnected from the specified adapter. This is particularly convenient for the dynamic controller model, where the mapping subsystemNQN &amp;lt;-&amp;gt; ctrlNumber is expected to be 1:1. If controllerNumber is also specified, this value is ignored.  ***Since:*** vSphere API 7.0  | [optional] 
**controller_number** | **int** | Controller number of the controller to be disconnected.  If this value is set, the subsystemQualifiedName can be left unset and the controller whose controllerNumber field matches this value will be disconnected from the specified adapter. If this value is not set, subsystemQualifiedName must be set.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nvme_disconnect_spec import HostNvmeDisconnectSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeDisconnectSpec from a JSON string
host_nvme_disconnect_spec_instance = HostNvmeDisconnectSpec.from_json(json)
# print the JSON string representation of the object
print HostNvmeDisconnectSpec.to_json()

# convert the object into a dict
host_nvme_disconnect_spec_dict = host_nvme_disconnect_spec_instance.to_dict()
# create an instance of HostNvmeDisconnectSpec from a dict
host_nvme_disconnect_spec_form_dict = host_nvme_disconnect_spec.from_dict(host_nvme_disconnect_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


