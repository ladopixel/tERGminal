<h1>tERGminal</h1>
<img src='https://camo.githubusercontent.com/ec19f4f188a819aea16eab8fb5d11c3916eda23f447e34ec2e03a57a321d7f38/68747470733a2f2f6572676f706c6174666f726d2e6f72672f696d672f6c6f676f747970655f77686974652e737667' alt='logo Ergo'>
<p>Simple application written in python to interact with the <a href='https://ergoplatform.org/en/'>Ergo blockchain</a> from the terminal.<br> 
Undoubtedly, the <a href="https://github.com/mgpai22/ergpy">ergpy repository</a> has been fundamental for the creation of <strong>tERGminal.</strong></p>

<img src='https://ergotokens.org/captura-tERGminal.png' alt='tERGminal screenshot'>


<h2>Quick Start</h2>

<h3>Prepare installation</h3>

~~~
sudo apt update && sudo apt upgrade -y
sudo apt install git pip openjdk-8-jre -y
~~~

<h4>Pi Zero</h4>

We need to explicity call Java 8 otherwise you will receive a "Server VM is only supported on ARMv7+ VFP" error. To correct this run the following ([credit](https://raspberrypi.stackexchange.com/questions/104203/unable-to-run-java-on-raspberry-pi-zero-vm-is-only-supported-on-armv7-vfp)): 

~~~
sudo update-alternatives --config java
# Then select Java 8's menu number
~~~

<h3>Install dependencies</h3>

~~~
pip install JPype1 ergpy
~~~

<h3>Clone repo</h3>

~~~
git clone https://github.com/ladopixel/tERGminal.git
~~~

<h3>Launch tERGminal</h3>

~~~
cd tERGminal
python ergpyMenu.py
~~~

<h2>Progress</h2>
<ul>
  <li>✅ 1 Configure wallet.</li>
  <li>✅ 2 Send ERG to a wallet.</li>
  <li>✅ 3 Send ERG to a random wallet (It use the array with addresses that appear in the whiteList.py file).</li>
  <li>✅ 4 Send NFT to wallet.</li>
  <li>✅ 5 Send NFT to a random wallet (It use the array with addresses that appear in the whiteList.py file).</li>
  <li>✅ 6 Send NFT random to a wallet.</li>
  <li>✅ 7 Create token.</li>
  <li>✅ 8 Create NFT.</li>
  <li>✅ 9 Info Ergo.</li>
  <li>✅ 10 Info Wallet.</li>
  <li>✅ 11 Info Token.</li>
  <li>✅ 12 Info transaction.</li>
  <li>✅ 13 Send tokens to multiple addresses (It use the array with addresses that appear in the whiteList.py file).</li>
  <li>✅ 14 Send multiple tokens to one address.</li>
  <li>✅ 15 Burn tokens.</li>
  <li>✅ 0 Exit.</li>
</ul>


<h2>Modifications</h2>
<p>The application is divided into 3 files:</p>
<ul>
  <li>ergpyMenu.py</li>
  <li>colorsPython.py</li>
  <li>whiteList.py</li>
</ul>
<p>There is not much to explain about these three files, <code>colorsPython.py</code> is for the graphic part on the screen, <code>whiteList.py</code> is the place where the addresses for the random wallet options are added and <code>ergpyMenu.py</code> is the file that contains the logic. </p>

<p>Feel free to make all the modifications you want to find out how it really works. Ask any questions.</p>

<h2>Usage</h2>
<p>Most of the options offered by this application are covered by the <a href='https://ergoplatform.org/en/get-erg/#Wallets'>official Ergo wallets.</a> The main idea that crossed my mind for the creation of tERGminal is to be able to carry a Swiss army knife of ERGO on a Raspberry Pi Zero when traveling. <br>tERGminal does not store any type of data, you can check it yourself by looking at its code before executing it.</p>
<p>Remember that this is a <strong>non-audit application,</strong> although I want you to have no problems with your ERGs, I recommend that the seed phrase you enter (it will never be stored) corresponds to a wallet that is not your main wallet.</p>
<p>For the options that display information (9, 10 and 11) there is no need to configure the wallet.</p>


