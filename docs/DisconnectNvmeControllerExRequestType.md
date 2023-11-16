# DisconnectNvmeControllerExRequestType

The parameters of *HostStorageSystem.DisconnectNvmeControllerEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disconnect_spec** | [**List[HostNvmeDisconnectSpec]**](HostNvmeDisconnectSpec.md) | A list of data objects, each specifying the parameters necessary to disconnect an NVMe controller.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.disconnect_nvme_controller_ex_request_type import DisconnectNvmeControllerExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectNvmeControllerExRequestType from a JSON string
disconnect_nvme_controller_ex_request_type_instance = DisconnectNvmeControllerExRequestType.from_json(json)
# print the JSON string representation of the object
print DisconnectNvmeControllerExRequestType.to_json()

# convert the object into a dict
disconnect_nvme_controller_ex_request_type_dict = disconnect_nvme_controller_ex_request_type_instance.to_dict()
# create an instance of DisconnectNvmeControllerExRequestType from a dict
disconnect_nvme_controller_ex_request_type_form_dict = disconnect_nvme_controller_ex_request_type.from_dict(disconnect_nvme_controller_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


