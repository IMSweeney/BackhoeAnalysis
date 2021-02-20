import ikpy
import numpy as np
import ikpy.utils.plot as plot_utils

from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink

import matplotlib.pyplot as plt

import importlib
importlib.import_module('mpl_toolkits').__path__
from mpl_toolkits.mplot3d import Axes3D


def example_chain():
    left_arm_chain = Chain(name='left_arm', links=[
        OriginLink(),
        URDFLink(
          name="shoulder",
          translation_vector=[-10, 0, 5],
          orientation=[0, 1.57, 0],
          rotation=[0, 1, 0],
        ),
        URDFLink(
          name="elbow",
          translation_vector=[25, 0, 0],
          orientation=[0, 0, 0],
          rotation=[0, 1, 0],
        ),
        URDFLink(
          name="wrist",
          translation_vector=[22, 0, 0],
          orientation=[0, 0, 0],
          rotation=[0, 1, 0],
        )
    ])
    return left_arm_chain


class BackhoeDefinition():

    def __init__(self):
        # More at:
        #   https://www.ritchiespecs.com/model/komatsu-pc2000-8-shovel

        # Backhoe Boom / Stick 1
        self.M = 9.235   # [m] Max Dig Depth
        self.L = 2.710   # [m] Max Vertical Wall Dig Depth
        self.Q = 12.310  # [m] Max Cutting Height
        self.R = 8.650   # [m] Max Dump Height

        self.arm_crowd_force = 574  # [Nm]
        self.backhoe_boom = 8.700   # [m]
        self.backhoe_stick = 3.900  # [m]
        self.max_reach_on_ground = 15.305  # [m]

        # Dimensions
        self.B = 5.410  # [m] Width over tracks
        self.D = 5.780  # [m] Length of track on ground
        self.G = 7.030  # [m] Height to top of cab
        self.E = 0.825  # [m] Ground Clearance

        self.length_of_tracks = 7.445  # [m]
        self.upper_structure_ground_clearance = 2.095  # [m]

        # Loading Shovel
        self.S = 13.170     # [m] Max dig reach
        self.R = 9.665      # [m] Max dump height
        self.Q = 14.450     # [m] Max cutting height
        self.T = 3.190      # [m] Max dig depth

        self.arm_crowd_force = 755          # [Nm]
        self.loading_shovel_boom = 5.950    # [m]
        self.loading_shovel_stick = 4.450   # [m]

    def get_links(self):
        pass


def backhoe():
    backhoe_def = BackhoeDefinition()
    # Actuators
    # Origin is at bottom link of boom piston
    chain = Chain(name='backhoe', links=[
        OriginLink(),
        URDFLink(
          name="boom",
          bounds=(0, 90),
          translation_vector=[0, 0, 0],
          orientation=[0, 0, 0],
          rotation=[0, 1, 0],
        ),
        URDFLink(
          name="stick",
          translation_vector=[25, 0, 0],
          orientation=[0, 0, 0],
          rotation=[0, 1, 0],
        ),
        URDFLink(
          name="bucket",
          translation_vector=[22, 0, 0],
          orientation=[0, 0, 0],
          rotation=[0, 1, 0],
        )
    ])
    return chain
    pass


if __name__ == '__main__':
    chain = example_chain()
    # pos = chain.forward_kinematics([0] * 7)

    target = [2, 2, 2]
    chain.inverse_kinematics(target)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    chain.plot(chain.inverse_kinematics(target), ax)
    plt.show()
    pass
