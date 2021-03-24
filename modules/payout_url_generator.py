#------------------------------------------------------------------------------------------------#
#  Payout URL Generator --- To be used with oTree --- Tested using Python 3.9.2
#------------------------------------------------------------------------------------------------#
#  payout_url_generator.py
#  DICE-Lab Payment Platform
#
#  Created by Leon Heidelbach on 24.03.2021.
#  Copyright © 2021 Leon Heidelbach. All rights reserved.
#
#------------------------------------------------------------------------------------------------#

# Import dependencies
# Absolute imports
import base64
import json

DEFAULT_BASE_URL : str =  'https://www3.hhu.de/lab/dice.php'
DEFAULT_CURRVIEW : str = 'paymentdatasubmitform'

class PayoutURLGenerator():
    '''
        The PayoutURLGenerator creates all parts of a payment URL objects and combines them into a URL-String.
        
        Usage:

            # Method 1.
            paymentURLGenerator = PayoutURLGenerator()
            paymentURLGenerator.setExpShortName("TestExp")
            paymentURLGenerator.setExpId(0000000000)
            paymentURLGenerator.setPid("XXXXXXXXXXXXXXX")
            paymentURLGenerator.setPayout(10.10)
            paymentURL = paymentURLGenerator.getPayoutURL()

            # Method 2.
            paymentURL = PayoutURLGenerator("TestExp",0000000000,"XXXXXXXXXXXXXXX",10.10).getPayoutURL()
        
            # Method 3.
            paymentURL = PayoutURLGenerator("TestExp","0000000000","XXXXXXXXXXXXXXX",10.10).getPayoutURL()

        Parameters:

            expShortName (str)  # The short name for the experiment as displayed on the experiment/session page of the payment platform.
            expId (int | str)   # The ORSEE experiment Id.
            pid (int | str)     # The ORSEE crypt participant Id.
            payout (float)      # The participant's payout amount for the current experiment. If no parameter is supplied, the payout parameter will be excluded from the url.
            baseURL (str)       # The base URL to the payment platform. DEFAULT: "https://www3.hhu.de/lab/dice.php".
    '''
    
    # Public methods

    def __init__(self, expShortName : str = None, expId : str = None, pid : str = None, payout : float = None, baseURL : str = DEFAULT_BASE_URL):
        self.expShortName = expShortName
        self.expId : str = str(expId)
        self.pid : str = str(pid)
        self.payout : float = payout
        self.baseURL : str = baseURL
        self.payoutURL : str = None
        self.currView : str = DEFAULT_CURRVIEW

    ## Getter methods

    def getPayoutURL(self) -> str:
        '''Returns the payout url for the initialized parameters.'''
        expBase64DictStr : str = self.__encodeBase64(json.dumps(self.__createExpDict()))
        self.payoutURL = f'{self.baseURL}?{self.getCurrViewParam()}&{self.getPidParam()}&{self.getExpIdParam()}'
        return self.payoutURL
    
    def getCurrViewParam(self) -> str:
        '''Returns the currView URL parameter -> "currView=XXXXXXX".'''
        return f'currView={self.currView}'
    
    def getPidParam(self) -> str:
        '''Returns the pid URL parameter -> "pid=XXXXXXX".'''
        return f'pid={self.pid}'
    
    def getExpIdParam(self) -> str:
        '''Returns the expId URL parameter -> "expId=XXXXXXX".'''
        return f'expId={self.__encodeBase64(json.dumps(self.__createExpDict()))}'
    
    ## Setter methods
    
    def setExpShortName(self, expShortName : str) -> None:
        '''Set the experiment short name parameter for the url generator'''
        self.expShortName = expShortName
    
    def setExpId(self, expId : any) -> None:
        '''Set the expId parameter for the url generator'''
        self.expId = str(expId)
    
    def setPid(self, pid : any) -> None:
        '''Set the pid parameter for the url generator'''
        self.pid = str(pid)
    
    def setPayout(self, payout : float) -> None:
        '''Set the payout amount parameter for the url generator'''
        self.payout = payout
    
    def setBaseUrl(self, baseURL : str) -> None:
        '''Set the baseURL parameter for the url generator'''
        self.baseURL = baseURL

    # Private methods

    def __encodeBase64(self, expDictStr : str) -> str:
        '''Returns a base64 encoded string.'''
        message_bytes : bytes = expDictStr.encode()
        base64_bytes : bytes = base64.b64encode(message_bytes)
        base64_message : str = base64_bytes.decode()
        return base64_message

    def __createExpDict(self) -> dict:
        '''Returns an experiment dictionary that contains a formatted form of the initialized parameters suited for the usage with the payment platform.'''
        expDict : dict = {
            "expData" : [
                {
                    "id" : self.expId,
                    "name" : self.expShortName,
                }
            ],
            "selected" : 0
        }

        if not self.payout == None:
            expDict['expData'][0]['payout'] = self.payout
        
        return expDict