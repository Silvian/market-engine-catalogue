#!/usr/bin/env python3

import grpc

import pb2.catalogue_pb2 as catalogue
import pb2.catalogue_pb2_grpc as catalogue_grpc

from concurrent import futures


class CatalogueService(catalogue_grpc.CatalogueServicer):
    def listCatalogueItems(self, request, context):
        item = catalogue.Item(
            id="73030316-ffc9-49d7-b524-0595ee49d93e",
            name="Pencil",
            image="https://cdn.mos.cms.futurecdn.net/3h95xxUbZTuCi54HWx8bjG-970-80.jpg.webp",
            rating=4.5,
        )
        return catalogue.Items(items=[item])

    def getItemDetails(self, request, context):
        return catalogue.ItemDetails(
            id="73030316-ffc9-49d7-b524-0595ee49d93e",
            name="Pencil",
            image="https://cdn.mos.cms.futurecdn.net/3h95xxUbZTuCi54HWx8bjG-970-80.jpg.webp",
            rating=4.5,
            description="This is a pretty cool pencil.",
            reviews=[],
        )


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    catalogue_grpc.add_CatalogueServicer_to_server(CatalogueService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()


def main():
    print("Running server...")
    run()


if __name__ == "__main__":
    main()
