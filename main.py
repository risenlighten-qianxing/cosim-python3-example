import grpc

from risenlighten.lasvsim.process_task.api.cosim.v1 import simulation_pb2
from risenlighten.lasvsim.process_task.api.cosim.v1 import simulation_pb2_grpc


def run():  # 8.146.201.197:30080 31244

    # 加载 TLS 证书
    credentials = grpc.ssl_channel_credentials(
        root_certificates=open(
            'qianxing-grpc.risenlighten.com_public.crt', 'rb').read()
    )

    # token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjcsIm9pZCI6MTAyLCJuYW1lIjoi572X5b-X5rSqIiwiaWRlbnRpdHkiOiJub3JtYWwiLCJwZXJtaXNzaW9ucyI6WyJ0YXNrLnRhc2sucHVibGljLkFDVElPTl9WSUVXIiwidGFzay50YXNrLnB1YmxpYy5BQ1RJT05fQ09QWSIsInRhc2sudGFzay5wdWJsaWMuQUNUSU9OX0RFTEVURSIsInRhc2sudGFzay5wdWJsaWMuQUNUSU9OX1JFUExBWSIsInRhc2sudGFzay5wdWJsaWMuQUNUSU9OX1JFUE9SVCIsInRhc2sudGFzay5wcml2YXRlLkFDVElPTl9WSUVXIiwidGFzay50YXNrLnByaXZhdGUuQUNUSU9OX0FERCIsInRhc2sudGFzay5wcml2YXRlLkFDVElPTl9DT1BZIiwidGFzay50YXNrLnByaXZhdGUuQUNUSU9OX0RFTEVURSIsInRhc2sudGFzay5wcml2YXRlLkFDVElPTl9SRVBMQVkiLCJ0YXNrLnRhc2sucHJpdmF0ZS5BQ1RJT05fUkVQT1JUIiwidGFzay50YXNrLnBlcnNvbmFsLkFDVElPTl9WSUVXIiwidGFzay50YXNrLnBlcnNvbmFsLkFDVElPTl9ERUxFVEUiLCJ0YXNrLnRhc2sucGVyc29uYWwuQUNUSU9OX1JFUExBWSIsInRhc2sudGFzay5wZXJzb25hbC5BQ1RJT05fUkVQT1JUIiwicmVzb3VyY2UudmVoaWNsZS5wdWJsaWMuQUNUSU9OX1ZJRVciLCJyZXNvdXJjZS52ZWhpY2xlLnB1YmxpYy5BQ1RJT05fVVBEQVRFIiwicmVzb3VyY2UudmVoaWNsZS5wdWJsaWMuQUNUSU9OX0RFTEVURSIsInJlc291cmNlLnZlaGljbGUucHVibGljLkFDVElPTl9VU0UiLCJyZXNvdXJjZS52ZWhpY2xlLnByaXZhdGUuQUNUSU9OX1ZJRVciLCJyZXNvdXJjZS52ZWhpY2xlLnByaXZhdGUuQUNUSU9OX0FERCIsInJlc291cmNlLnZlaGljbGUucHJpdmF0ZS5BQ1RJT05fVVBEQVRFIiwicmVzb3VyY2UudmVoaWNsZS5wcml2YXRlLkFDVElPTl9ERUxFVEUiLCJyZXNvdXJjZS52ZWhpY2xlLnByaXZhdGUuQUNUSU9OX1VTRSIsInJlc291cmNlLnZlaGljbGUucGVyc29uYWwuQUNUSU9OX1ZJRVciLCJyZXNvdXJjZS52ZWhpY2xlLnBlcnNvbmFsLkFDVElPTl9VUERBVEUiLCJyZXNvdXJjZS52ZWhpY2xlLnBlcnNvbmFsLkFDVElPTl9ERUxFVEUiLCJyZXNvdXJjZS5zZW5zb3IucHVibGljLkFDVElPTl9WSUVXIiwicmVzb3VyY2Uuc2Vuc29yLnB1YmxpYy5BQ1RJT05fVVBEQVRFIiwicmVzb3VyY2Uuc2Vuc29yLnB1YmxpYy5BQ1RJT05fREVMRVRFIiwicmVzb3VyY2Uuc2Vuc29yLnB1YmxpYy5BQ1RJT05fVVNFIiwicmVzb3VyY2Uuc2Vuc29yLnByaXZhdGUuQUNUSU9OX1ZJRVciLCJyZXNvdXJjZS5zZW5zb3IucHJpdmF0ZS5BQ1RJT05fQUREIiwicmVzb3VyY2Uuc2Vuc29yLnByaXZhdGUuQUNUSU9OX1VQREFURSIsInJlc291cmNlLnNlbnNvci5wcml2YXRlLkFDVElPTl9ERUxFVEUiLCJyZXNvdXJjZS5zZW5zb3IucHJpdmF0ZS5BQ1RJT05fVVNFIiwicmVzb3VyY2Uuc2Vuc29yLnBlcnNvbmFsLkFDVElPTl9WSUVXIiwicmVzb3VyY2Uuc2Vuc29yLnBlcnNvbmFsLkFDVElPTl9VUERBVEUiLCJyZXNvdXJjZS5zZW5zb3IucGVyc29uYWwuQUNUSU9OX0RFTEVURSIsInJlc291cmNlLm1hcC5wdWJsaWMuQUNUSU9OX1ZJRVciLCJyZXNvdXJjZS5tYXAucHVibGljLkFDVElPTl9VUERBVEUiLCJyZXNvdXJjZS5tYXAucHVibGljLkFDVElPTl9ERUxFVEUiLCJyZXNvdXJjZS5tYXAucHVibGljLkFDVElPTl9VU0UiLCJyZXNvdXJjZS5tYXAucHJpdmF0ZS5BQ1RJT05fVklFVyIsInJlc291cmNlLm1hcC5wcml2YXRlLkFDVElPTl9BREQiLCJyZXNvdXJjZS5tYXAucHJpdmF0ZS5BQ1RJT05fVVBEQVRFIiwicmVzb3VyY2UubWFwLnByaXZhdGUuQUNUSU9OX0RFTEVURSIsInJlc291cmNlLm1hcC5wcml2YXRlLkFDVElPTl9VU0UiLCJyZXNvdXJjZS5tYXAucGVyc29uYWwuQUNUSU9OX1ZJRVciLCJyZXNvdXJjZS5tYXAucGVyc29uYWwuQUNUSU9OX1VQREFURSIsInJlc291cmNlLm1hcC5wZXJzb25hbC5BQ1RJT05fREVMRVRFIiwicmVzb3VyY2Uuc2NlbmFyaW8ucHVibGljLkFDVElPTl9WSUVXIiwicmVzb3VyY2Uuc2NlbmFyaW8ucHVibGljLkFDVElPTl9DT1BZIiwicmVzb3VyY2Uuc2NlbmFyaW8ucHVibGljLkFDVElPTl9VUERBVEUiLCJyZXNvdXJjZS5zY2VuYXJpby5wdWJsaWMuQUNUSU9OX0RFTEVURSIsInJlc291cmNlLnNjZW5hcmlvLnB1YmxpYy5BQ1RJT05fVVNFIiwicmVzb3VyY2Uuc2NlbmFyaW8ucHJpdmF0ZS5BQ1RJT05fVklFVyIsInJlc291cmNlLnNjZW5hcmlvLnByaXZhdGUuQUNUSU9OX0NPUFkiLCJyZXNvdXJjZS5zY2VuYXJpby5wcml2YXRlLkFDVElPTl9VUERBVEUiLCJyZXNvdXJjZS5zY2VuYXJpby5wcml2YXRlLkFDVElPTl9ERUxFVEUiLCJyZXNvdXJjZS5zY2VuYXJpby5wcml2YXRlLkFDVElPTl9VU0UiLCJyZXNvdXJjZS5zY2VuYXJpby5wcml2YXRlLkFDVElPTl9BREQiLCJyZXNvdXJjZS5zY2VuYXJpby5wZXJzb25hbC5BQ1RJT05fVklFVyIsInJlc291cmNlLnNjZW5hcmlvLnBlcnNvbmFsLkFDVElPTl9VUERBVEUiLCJyZXNvdXJjZS5zY2VuYXJpby5wZXJzb25hbC5BQ1RJT05fREVMRVRFIiwicmVzb3VyY2UudHJhZmZpY19mbG93X2NvbmZpZy5wdWJsaWMuQUNUSU9OX1ZJRVciLCJyZXNvdXJjZS50cmFmZmljX2Zsb3dfY29uZmlnLnB1YmxpYy5BQ1RJT05fVVBEQVRFIiwicmVzb3VyY2UudHJhZmZpY19mbG93X2NvbmZpZy5wdWJsaWMuQUNUSU9OX0RFTEVURSIsInJlc291cmNlLnRyYWZmaWNfZmxvd19jb25maWcucHVibGljLkFDVElPTl9VU0UiLCJyZXNvdXJjZS50cmFmZmljX2Zsb3dfY29uZmlnLnByaXZhdGUuQUNUSU9OX1ZJRVciLCJyZXNvdXJjZS50cmFmZmljX2Zsb3dfY29uZmlnLnByaXZhdGUuQUNUSU9OX1VQREFURSIsInJlc291cmNlLnRyYWZmaWNfZmxvd19jb25maWcucHJpdmF0ZS5BQ1RJT05fREVMRVRFIiwicmVzb3VyY2UudHJhZmZpY19mbG93X2NvbmZpZy5wcml2YXRlLkFDVElPTl9VU0UiLCJyZXNvdXJjZS50cmFmZmljX2Zsb3dfY29uZmlnLnByaXZhdGUuQUNUSU9OX0FERCIsInJlc291cmNlLnRyYWZmaWNfZmxvd19jb25maWcucGVyc29uYWwuQUNUSU9OX1ZJRVciLCJyZXNvdXJjZS50cmFmZmljX2Zsb3dfY29uZmlnLnBlcnNvbmFsLkFDVElPTl9VUERBVEUiLCJyZXNvdXJjZS50cmFmZmljX2Zsb3dfY29uZmlnLnBlcnNvbmFsLkFDVElPTl9ERUxFVEUiXSwiaXNzIjoidXNlciIsInN1YiI6Ikxhc1ZTaW0iLCJleHAiOjE2OTE1NTMwNzksIm5iZiI6MTY5MTQ2NjY3OSwiaWF0IjoxNjkxNDY2Njc5LCJqdGkiOiI3In0.FBEmLEa843Yz1rKuyoWOZIyvpYuEGaaPdHC3xIQBhtw'
    token = ''
    metadata = [('authorization', 'Bearer ' + token)]

    with grpc.secure_channel('qianxing-grpc.risenlighten.com', credentials) as channel:
        # with grpc.insecure_channel('8.146.201.197:30081') as channel:
        # with grpc.insecure_channel('120.46.203.61:9001') as channel:
        stub = simulation_pb2_grpc.CosimStub(channel)
        startResp = stub.Start(
            simulation_pb2.StartSimulationReq(task_id=4174, record_id=2429), metadata=metadata)

        while True:
            # 获取自车以及自车的周车列表
            vehicle = stub.GetVehicle(simulation_pb2.GetVehicleReq(
                simulation_id=startResp.simulation_id, vehicle_id='ego'), metadata=metadata)
            checkError(vehicle.error)

            # vehicleControleReult = stub.SetVehicleControl(simulation_pb2.SetVehicleControlReq(
            #     simulation_id=startResp.simulation_id, vehicle_id='ego', lon_acc=1, ste_wheel=1))
            # checkError(vehicleControleReult.error)

            stepResult = stub.NextStep(simulation_pb2.NextStepReq(
                simulation_id=startResp.simulation_id), metadata=metadata)
            if checkError(stepResult.error):
                break

            # 状态不正确，结束
            if (stepResult.state.progress < 0) or (stepResult.state.progress >= 100):
                print(
                    f"仿真结束,状态：{stepResult.state.msg}")
                break

        stub.ResetSimulation(simulation_pb2.ResetSimulationReq(
            simulation_id=startResp.simulation_id), metadata=metadata)

        stub.NextStep(simulation_pb2.NextStepReq(
            simulation_id=startResp.simulation_id), metadata=metadata)

        print(
            f"id：{startResp.simulation_id}")
        stub.Stop(simulation_pb2.StopSimulationReq(
            simulation_id=startResp.simulation_id), metadata=metadata)
        result = stub.GetResults(simulation_pb2.GetResultsReq(
            simulation_id=startResp.simulation_id), metadata=metadata)
        # print(f"仿真结束,结果:{result.results}")


def checkError(err):
    if err is None:
        return False

    if err.code != 0:
        print(err.msg)
        return True
    return False


if __name__ == '__main__':
    run()
