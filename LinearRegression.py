import sys
from typing import *


class LinearRegressor:
  """
  For now I,ll limit the capability to 1 input and 1 output only
  """
  def __init__(self, args, learning_rate : int = 0.01):
    self.learned : list[bool,str] = [False,'']
    self.__slope : int = 0
    self.__intercept : int = 0
    self.learning_rate = learning_rate
    self.valid_input(args)
    self.linearregressor(args)

  @staticmethod
  def valid_input(args):
    # Have to add functionality to include multiple inputs
    try:
      print(type(args))
      if len(args.iloc[0])==2:
        if len(args.iloc[:,0])-len(args.iloc[:,1])!=0 :
          sys.exit("Input and Output data columns length must be same ")
      else:
        sys.exit("The class currently only supports 1 input and 1 output")
    except Exception as e:
      print("Error:",e)

  def Predict(self,x):
    return self.__slope * x + self.__intercept

  @overload
  def diff(self, b : int, args,slope = None ,yintercept = None):
    summ = 0
    for i in range(len(args.iloc[:,0])):
      hx = self.line(args.iloc[i,0] ,slope ,yintercept)
      yx = args.iloc[i:1]
      summ += hx - yx
    return summ

  @overload
  def diff(self,b : str, args,slope = None,yintercept = None):
    summ = 0
    for i in range(len(args.iloc[:,0])):
      hx = self.line(args.iloc[i,0] ,slope ,yintercept)
      yx = args.iloc[i:1]
      summ += ( hx - yx ) * args.iloc[i,0]
    return summ

  def diff(self,b,args,slope = None , yintercept = None):
    pass

  def line(self,x, m : int = 0, b : int = 0):
    m = self.__slope
    b = self.__intercept
    return m*x + b

  @staticmethod
  def convergence(*args,e=0.009) -> bool:
    # does not check if the incoming values are in correct pairs or not , it may accidently subtract slope and intercept ,
    # if i passed that to this func
    if len(args)!=2:
      sys.exit("Only 2 values can be sent into convergence at once")
    else:
      print(args[0],args[1])
      if abs(args[0]-args[1]) <= e:
        return True
      else:
        return False

  def linearregressor(self,args) -> LinearRegressor:
    theta0 = self.__intercept
    theta1 = self.__slope
    a = b = 100
    print('hi')
    while True:
      print('hii')
      print((self.convergence(a,theta0),self.convergence(b,theta1)))
      if (self.convergence(a,theta0),self.convergence(b,theta1))==(False,False):
        print('a')
        a = theta0
        theta0 = theta0 - self.learning_rate*(1/len(args.iloc[:,0])) * self.diff(1, yintercept = theta0, slope = theta1)
        b = theta1
        theta1 = theta1 - self.learning_rate*(1/len(args.iloc[:,0])) * self.diff('', yintercept = theta0, slope = theta1)

      elif (self.convergence(a,theta0),self.convergence(b,theta1))==(True,False):
        print('b')
        b = theta1
        theta1 = theta1 - self.learning_rate*(1/len(args.iloc[:,0])) * self.diff('', yintercept = theta0, slope = theta1)

      elif (self.convergence(a,theta0),self.convergence(b,theta1))==(False,True):
        print('c')
        a = theta0
        theta0 = theta0 - self.learning_rate*(1/len(args.iloc[:,0])) * self.diff(1, yintercept = theta0, slope = theta1)
      else:
        print('d')
        break

    print('welcome')

    self.__intercept = theta0
    self.__slope = theta1
    self.learned = [ True , f"y={theta1}*x + {theta0}"]
    return self



