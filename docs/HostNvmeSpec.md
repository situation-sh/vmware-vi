# HostNvmeSpec

Specifies the main parameters needed when connecting to an NVMe over Fabrics controller or Discovery Service.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hba_name** | **str** | The device name of the NVME over Fabrics host bus adapter.  ***Since:*** vSphere API 7.0  | 
**transport_parameters** | [**HostNvmeTransportParameters**](HostNvmeTransportParameters.md) |  | 

## Example

```python
from vmware_vi.models.host_nvme_spec import HostNvmeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeSpec from a JSON string
host_nvme_spec_instance = HostNvmeSpec.from_json(json)
# print the JSON string representation of the object
print HostNvmeSpec.to_json()

# convert the object into a dict
host_nvme_spec_dict = host_nvme_spec_instance.to_dict()
# create an instance of HostNvmeSpec from a dict
host_nvme_spec_form_dict = host_nvme_spec.from_dict(host_nvme_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


